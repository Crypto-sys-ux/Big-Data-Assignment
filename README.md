# Customer Analytics Pipeline

## Description
This project implements a full data analytics pipeline using Docker. The pipeline processes a raw dataset, performs preprocessing, generates insights, visualizations, and clustering results.

## Dataset
Mall Customer Segmentation Dataset

## How to Build
docker build -t customer-analytics .

## How to Run
docker run -it customer-analytics

Inside container:
python ingest.py dataset.csv

## Pipeline Flow
1. ingest.py → loads dataset
2. preprocess.py → cleans and transforms data
3. analytics.py → generates insights
4. visualize.py → creates plots
5. cluster.py → applies K-Means clustering

## Output Files
- data_raw.csv
- data_preprocessed.csv
- insight1.txt
- insight2.txt
- insight3.txt
- summary_plot.png
- clusters.txt

## Notes
All steps are executed automatically in sequence inside Docker.

## Docker Hub
https://hub.docker.com/r/r2a3d/customer-analytics

## Team Members
(Shehab Hegazy)
