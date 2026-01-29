print('started script')
import numpy as np
import xarray as xr
import dask.array as da
from datetime import datetime
import os
import glob
from dask.distributed import Client, LocalCluster

# Directories-----
# Check where the script is running
host_name = os.popen('hostname').read().strip()
if host_name == 'falcon.local': #if on my computer, create a tiny subset of the data to perform an EOF on (used for code development)
    SAVE_DIRECTORY = '/Users/kathum/Research/COPEX/eof_analysis_data/'
    DATA_DIRECTORY = '/Users/kathum/Research/COPEX/aggregated_files/wam_output/aggregated_co_altclimate_nfr_2000_2023/'
    max_lon, min_lon, max_lat, min_lat = (250.0-15, 258.0+10, 37.0-10, 41.0+10)  # Colorado subset
else:
    SAVE_DIRECTORY = '/home/kathum/EOF_output/'
    DATA_DIRECTORY = '/home/kathum/wam_aggregated_files/'
    max_lon, min_lon, max_lat, min_lat = (180.0, 359.75, 0.0, 70.0)  # larger area

#modify--------------------
months = [5, 6, 7] # Select months
#--------------------------

#dask client activation
cluster = LocalCluster(n_workers=64, memory_limit="auto" )
client = Client(cluster)
print('dask client has be created---')
print(client)
print('---------')

# open aggregated datasets
files = sorted([f for month_num in months for f in glob.glob(DATA_DIRECTORY + f"*-{month_num:02}.nc")])
raw_data = xr.open_mfdataset(files, chunks={"time": 1})['e_track']
raw_data = raw_data.resample(time='1YE').sum().sel(latitude=slice(min_lat, max_lat), longitude=slice(max_lon, min_lon))
print('finished loading rawdata')

# Compute e-track anomaly 
anomaly_data = raw_data - raw_data.mean(dim="time")

# Convert to 2D array
X_dask = anomaly_data.stack(gridcell=("latitude", "longitude")).transpose("time", "gridcell").data
X = X_dask.compute() #get numpy array

#Calculate covariance 
C = da.tensordot(X_dask.T, X_dask, axes=(1, 0)) / X_dask.shape[0]
C = (C + C.T) / 2  # Ensure symmetry
C = C.persist()  
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

# Convert eigenvalues to percent variance explained
pve = 100.0 * lam / lam.sum()

#Save Results 
np.savetxt(f'{SAVE_DIRECTORY}lam_large.csv', lam, delimiter=',')
print('saved lam')
np.savetxt(f'{SAVE_DIRECTORY}E_large.csv', E, delimiter=',')
print('saved E')
np.savetxt(f'{SAVE_DIRECTORY}Z_large.csv', Z, delimiter=',')
print('saved Z')
np.savetxt(f'{SAVE_DIRECTORY}pve_large.csv', pve, delimiter=',')
print('saved pve')
np.savetxt(f'{SAVE_DIRECTORY}i_large.csv', i, delimiter=',')
print('saved i')
np.savetxt(f'{SAVE_DIRECTORY}X_large.csv', X, delimiter=',')
print('saved X')

# Save lat/lon dimensions
np.savetxt(f'{SAVE_DIRECTORY}latitude_large.csv', raw_data.latitude.values, delimiter=',')
np.savetxt(f'{SAVE_DIRECTORY}longitude_large.csv', raw_data.longitude.values, delimiter=',')

print(f"Finished computation on {datetime.today().strftime('%m_%d_%Y')} at {datetime.today().strftime('%H:%M:%S')}")
