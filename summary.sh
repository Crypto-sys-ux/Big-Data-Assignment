#!/bin/bash

CONTAINER_NAME="customer-analytics-run"

mkdir -p customer-analytics/results

docker cp $CONTAINER_NAME:/app/pipeline/data_raw.csv          customer-analytics/results/
docker cp $CONTAINER_NAME:/app/pipeline/data_preprocessed.csv customer-analytics/results/
docker cp $CONTAINER_NAME:/app/pipeline/insight1.txt          customer-analytics/results/
docker cp $CONTAINER_NAME:/app/pipeline/insight2.txt          customer-analytics/results/
docker cp $CONTAINER_NAME:/app/pipeline/insight3.txt          customer-analytics/results/
docker cp $CONTAINER_NAME:/app/pipeline/clusters.txt          customer-analytics/results/
docker cp $CONTAINER_NAME:/app/pipeline/summary_plot.png      customer-analytics/results/

echo "✅ All files copied to customer-analytics/results/"

docker stop $CONTAINER_NAME
docker rm   $CONTAINER_NAME

echo "✅ Container stopped and removed"