#!/bin/bash

# Download necessary files
wget -O utils/compute_eval_statistics.py https://storage.googleapis.com/nutrition5k_dataset/nutrition5k_dataset/scripts/compute_eval_statistics.py
wget -O resources/dish_metadata_cafe1.csv https://storage.googleapis.com/nutrition5k_dataset/nutrition5k_dataset/metadata/dish_metadata_cafe1.csv
wget -O resources/dish_metadata_cafe2.csv https://storage.googleapis.com/nutrition5k_dataset/nutrition5k_dataset/metadata/dish_metadata_cafe2.csv
wget -O resources/ingredients_metadata.csv https://storage.googleapis.com/nutrition5k_dataset/nutrition5k_dataset/metadata/ingredients_metadata.csv
wget -O resources/dish_ids_cafe1.txt https://storage.googleapis.com/nutrition5k_dataset/nutrition5k_dataset/dish_ids/dish_ids_cafe1.txt

echo "Files downloaded successfully."
