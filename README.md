# NutriGen

**NutriGen** is a smart food recommendation system which recommend a smart weekly menu for people due to their personal information: age, weight, gender, ...

# Our system interface

# About us

Our team belong to Ho Chi Minh University of Technology at Intelligent System subject's project, contain:

-   [Huynh Dai Vinh](https://github.com/02david20)
-   [Doan Tran Cao Tri](https://github.com/tri218138)

# Methology

Our proposal system using AI model: Genetic Algorithm for recommending since its performance, fast and reliable

## Genetic Algorithm

### Objective Function

## Web System

# Evaluation

| Generations | Training Time | Best Fitness | Best Individual                                    |
| ----------- | ------------- | ------------ | -------------------------------------------------- |
| 0           | 100           | 3.902461     | [dish_1551491048, dish_1558722125, dish_156659...] |
| 1           | 500           | 14.070692    | [dish_1561739160, dish_1551236949, dish_156330...] |
| 2           | 1000          | 21.264965    | [dish_1563221157, dish_1558376212, dish_155149...] |
| 3           | 5000          | 99.835112    | [dish_1562094931, dish_1563391922, dish_155931...] |

# How to use

Download food data from [Nutrition5k](https://github.com/google-research-datasets/Nutrition5k) dataset of Google

```bash
$wget -O utils/compute_eval_statistics.py https://storage.googleapis.com/nutrition5k_dataset/nutrition5k_dataset/scripts/compute_eval_statistics.py
$wget -O resources/dish_metadata_cafe1.csv https://storage.googleapis.com/nutrition5k_dataset/nutrition5k_dataset/metadata/dish_metadata_cafe1.csv
$wget -O resources/dish_metadata_cafe2.csv https://storage.googleapis.com/nutrition5k_dataset/nutrition5k_dataset/metadata/dish_metadata_cafe2.csv
$wget -O resources/ingredients_metadata.csv https://storage.googleapis.com/nutrition5k_dataset/nutrition5k_dataset/metadata/ingredients_metadata.csv
$wget -O resources/dish_ids_cafe1.txt https://storage.googleapis.com/nutrition5k_dataset/nutrition5k_dataset/dish_ids/dish_ids_cafe1.txt

```

Install neccessary library

```bash
$python -m pip install -r requirements.txt
```
