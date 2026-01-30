# Code for "Evaporative Moisture Sources of Colorado’s Front Range: A Case Study of the Exceptionally Wet May-July Season of 2023"

## Brief Summary
This repository holds all of the code needed to reporduce all figures in the manuscript, "Evaporative Moisture Sources of Colorado’s Front Range: A Case Study of the Exceptionally Wet May-July Season of 2023". The data used for these analyses can be found publically published in Dryad with the DOI: 10.5061/dryad.jsxksn0p3. 

## File List and Description

- *copex_env.yml*: YAML file used to define the specifications of the Python environment used for this project. 

- *create_region_info_csv.ipynb*: Python notebook that creates and saves a csv containing information about all sink/source regions. This csv is used in other notebooks for this analysis.

- *eof_analysis.py*: Python script that conducts an Empirical Orthogonal Function (EOF) analysis on anomalous moisture sources of Eastern Colorado precipitation.