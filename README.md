# Code for "Evaporative Moisture Sources of Colorado’s Front Range: A Case Study of the Exceptionally Wet May-July Season of 2023"

## Brief Summary
This repository holds all of the code needed to reporduce all figures in the manuscript, "Evaporative Moisture Sources of Colorado’s Front Range: A Case Study of the Exceptionally Wet May-July Season of 2023". The data used for these analyses can be found publically published in Dryad with the DOI: 10.5061/dryad.jsxksn0p3. 

## File List and Description

- *copex_env.yml*: YAML file used to define the specifications of the Python environment used for this project. 

- *create_region_info_csv.ipynb*: Python notebook that creates and saves a csv containing information about all sink/source regions. This csv is used in other notebooks for this analysis.

- *eof_analysis.py*: Python script that conducts an Empirical Orthogonal Function (EOF) analysis on anomalous moisture sources of Eastern Colorado precipitation. This script conducts the anlysis and saves output to multiple csv files. Visualization of EOF analysis can be found in the file,"figure9_10_visualize_eof_analysis.ipynb". Due to memory constraints, this script was intended to run on a high performance computer.

- *figure2_nfr_region_map.ipynb*: Python notebook that creates and saves a map depicting the Northern Front Range region of Colorado. Output from this notebook reproduces figure 2 in the associated manuscript. 

- *figure3_4_moisture_sources_map_barchart.ipynb*: Python notebook that summarizes the moisture sources of Eastern Colorado regions into a map and barcharts. Output from this notebook reporduces figures 3 and 4 in the associated manuscript.

- *figure5_percent_of_average.ipynb*:

- *figure6_elbow_method.ipynb*:

- *figure7_clustering_analysis.ipynb*:

- *figure8_variance_explained.ipynb*:

- *figure9_10_visualize_eof_analysis.ipynb*:

- *figureA.1.1_era5_prism_comp_scatter.ipynb*:

- *figureA.2.2_map_of_region_classification.ipynb*: