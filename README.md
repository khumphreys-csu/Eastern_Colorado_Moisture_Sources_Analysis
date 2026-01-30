# Code for "Evaporative Moisture Sources of Colorado’s Front Range: A Case Study of the Exceptionally Wet May-July Season of 2023"

## Brief Summary
This repository holds all of the code needed to reporduce all figures in the manuscript, "Evaporative Moisture Sources of Colorado’s Front Range: A Case Study of the Exceptionally Wet May-July Season of 2023". The data used for these analyses can be found publically published in Dryad with the DOI: 10.5061/dryad.jsxksn0p3. 

## File List and Description

- *copex_env.yml*: YAML file used to define the specifications of the Python environment used for this project. 

- *create_region_info_csv.ipynb*: Python notebook that creates and saves a csv containing information about all sink/source regions. This csv is used in other notebooks for this analysis.

- *eof_analysis.py*: Python script that conducts an Empirical Orthogonal Function (EOF) analysis on anomalous moisture sources of Eastern Colorado precipitation. This script conducts the anlysis and saves output to multiple csv files. Visualization of EOF analysis can be found in the file,"figure9_10_visualize_eof_analysis.ipynb". Due to memory constraints, this script was intended to run on a high performance computer.

- *figure2_nfr_region_map.ipynb*: Python notebook that creates and saves a map depicting the Northern Front Range region of Colorado. Output from this notebook reproduces figure 2 in the associated manuscript. 

- *figure3_4_moisture_sources_map_barchart.ipynb*: Python notebook that summarizes the moisture sources of Eastern Colorado regions into a map and barcharts. Output from this notebook reproduces figures 3 and 4 in the associated manuscript.

- *figure5_percent_of_average.ipynb*: Python notebook that visualizes each source region's percent of average contribution in 2023 as a barchart. Output from this notebook reproduces figure 5 in the associated manuscript.

- *figure6_elbow_method.ipynb*: Python notebook comparing k-means clustering performance across different k values using within-cluster sum of squared distances (WCSS) and the elbow method. Output from this notebook reproduces figure 6 in the associated manuscript.

- *figure7_clustering_analysis.ipynb*: Python notebook conducting a k-means clustering analysis on Eastern Colorado's moisture sources and visualizes results in maps and scatter plots. Output from this notebook reproduces figure 7 in the associated manuscript.

- *figure8_variance_explained.ipynb*: Python notebook that visualizes the fraction of variance explained by each eigenvector from the EOF analysis conducted in the eof_analysis.py script. Output from this notebook reproduces figure 8 in the associated manuscript.

- *figure9_10_visualize_eof_analysis.ipynb*: Python notebook that reads output from eof_analysis.py and visualizes the first and second principle components and eigen vectors as a map and a timeseries. Output from this notebook reproduces figures 9 and 10 in the associated manuscript.

- *figureA.1.1_era5_prism_comp_scatter.ipynb*: Python notebook that compares sink region monthly precipitation totals between ERA5 and PRISM precipitation products in the form of a scatterplot. Output from this notebook reproduces figure A.1.1 in the appendix of the associated manuscript.

- *figureA.1.2_A.1.3_era5_prism_rainfall_map_comparison.ipynb*: Python notebook that compares the spatial differences in monthly rainfall estimates between ERA5 and PRISM precipitation products. Output from this notebook reproduces figures A.1.2 and A.1.3 in the appendix of the associated manuscript.

- *figureA.2.1_sink_region_maps.ipynb*: Python notebook that produces a map of Colorado’s alternate climate divisions adapted to a 0.25°x0.25° latitude longitude grid (as described in Schumacher et al., 2024).

- *figureA.2.2_map_of_region_classification.ipynb*: 

- *figureA.3_sensitivity_analysis.ipynb*:

- *tables_1-4_code.ipynb*: