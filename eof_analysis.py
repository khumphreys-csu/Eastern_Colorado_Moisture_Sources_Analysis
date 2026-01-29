print('started script')
import numpy as np
import xarray as xr
import dask.array as da
from datetime import datetime
import os
import glob
#modify---------------------------
sink_region = 'sp' #nfr, se, ne, pp, sp
# Select months
months = [5, 6, 7]
# Directories
# Check where the script is running
host_name = os.popen('hostname').read().strip()
if host_name == 'falcon.local':
    SAVE_DIRECTORY = '/Users/kathum/Research/COPEX/eof_analysis_data/'
    DATA_DIRECTORY = '/Users/kathum/Research/COPEX/aggregated_files/wam_output/aggregated_co_altclimate_nfr_2000_2023/'
    max_lon, min_lon, max_lat, min_lat = (360.0-125, 360.0-92, 22.0, 46.0) 
else: #aka running on a super computer
    SAVE_DIRECTORY = f'/home/kathum/EOF_output/{sink_region}/'
    DATA_DIRECTORY = f'/home/kathum/wam_aggregated_files/{sink_region}/'
    max_lon, min_lon, max_lat, min_lat = (360.0-134, 360.0-67, 23.0, 49) # larger area
#--------------------------------

# Get files
files = sorted([f for month_num in months for f in glob.glob(DATA_DIRECTORY + f"*-{month_num:02}.nc")])

# Open dataset, aggregate to MJJ e-track, and filter latitude and longitude dimensions
raw_data = xr.open_mfdataset(files, chunks={"time": 1})['e_track']
raw_data = raw_data.resample(time='1YE').sum().sel(latitude=slice(min_lat, max_lat), longitude=slice(max_lon, min_lon))
print('finished loading rawdata')

# Compute anomaly 
anomaly_data = raw_data - raw_data.mean(dim="time")
anomaly_data = anomaly_data * (10**(-14))

# Convert to 2D array
X_dask = anomaly_data.stack(gridcell=("latitude", "longitude")).transpose("time", "gridcell").data
X = X_dask.compute() #get numpy array

#Covariance Calculation
C = da.tensordot(X_dask.T, X_dask, axes=(1, 0)) / X_dask.shape[0]
C = (C + C.T) / 2  # Ensure symmetry
C = C.compute() 
print('created C')

#Eigen decomposition
lam, E = np.linalg.eigh(C)
print('created lam, E')

# Sort eigenvalues and eigenvectors
i = np.argsort(-lam)
lam = lam[i]
E = E[:, i]

# Compute Principal Component time series
Z = da.dot(X_dask, E)
Z = Z.compute()  # Compute only at this step
Z_std = (Z-Z.mean(axis = 0))/Z.std(axis=0)
print('created Z')

#Compute E tilda (d) associated with std Zs
X_orig_units = X_dask * (10**14)
d1 = (1/X.shape[0])*(np.dot(np.transpose(Z_std[:,0]),X_orig_units)).compute()
d2 = (1/X.shape[0])*(np.dot(np.transpose(Z_std[:,1]),X_orig_units)).compute()
d3 = (1/X.shape[0])*(np.dot(np.transpose(Z_std[:,2]),X_orig_units)).compute()
print('created D')

# Convert eigenvalues to percent variance explained
pve = 100.0 * lam / lam.sum()

#-------Save important vectors-------
variables_to_save = {'lam':lam, 'i':i,'Z':Z_std, 'pve':pve, 'X':X, 'd1':d1, 'd2':d2, 'd3':d3}
for save_var in variables_to_save:
    np.savetxt(f'{SAVE_DIRECTORY}{save_var}_{datetime.today().strftime('%m_%d')}.csv', variables_to_save[save_var], delimiter=',')
    print(f'saved {save_var} on {datetime.today().strftime('%m_%d_%Y')} at {datetime.today().strftime('%H:%M:%S')}')

#save E1,2,3 and D1,2,3
eof_num = 3
for i in range(3):
    e_n = E[:, i]
    np.savetxt(f'{SAVE_DIRECTORY}e{i+1}_{datetime.today().strftime('%m_%d')}.csv', e_n, delimiter=',')
    print(f'saved EOF {i+1} on {datetime.today().strftime('%m_%d_%Y')} at {datetime.today().strftime('%H:%M:%S')}')
  
#save the lat/long values of the data
np.savetxt(f'{SAVE_DIRECTORY}latitude_{datetime.today().strftime('%m_%d')}.csv',raw_data.latitude.values, delimiter=',')
np.savetxt(f'{SAVE_DIRECTORY}longitude_{datetime.today().strftime('%m_%d')}.csv',raw_data.longitude.values, delimiter=',')
print(f'saved lat/lon count on {datetime.today().strftime('%m_%d_%Y')} at {datetime.today().strftime('%H:%M:%S')}')

#print end of the script
print(f"Finished computation on {datetime.today().strftime('%m_%d_%Y')} at {datetime.today().strftime('%H:%M:%S')}")