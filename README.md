# NYC Second Ave Subway: Impact in taxi ridership

This is an updated version of the work we did with our group for the December 2018 Hackathon at CUSP.

We used timeseries analysis and point of change detection to assess the impact of the NYC Second Ave Subway openning in taxi ridership in the area.

## Data Processing

The Jupyter Notebook [data_processing.ipynb](data_processing.ipynb) downloads 3 years of NYC yellow taxi data from the TLC and preprocesses it to get a timeseries with daily pickups in the Taxi Zones arround the Second Ave Subway. The TLC uploads a dataset of 1-2gb for each month so the data processing takes a few hours. The final file is [yellowtaxi_all.csv](yellowtaxi_all.csv).

## Data Exploration and Analysis

The Jupyter Notebook [data_analysis.ipynb](data_analysis.ipynb) has the analysis of the timeseries: periodicity, seasonality and trend, and finally point of change detection using bayesian inference.
