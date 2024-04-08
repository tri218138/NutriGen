import json
from os import path
import statistics
import sys
from pathlib import Path

__dir__ = Path.cwd()

DISH_ID_INDEX = 0
DATA_FIELDNAMES = ["dish_id", "calories", "mass", "fat", "carb", "protein"]


def ReadCsvData(filepath):
    if not path.exists(filepath):
        raise Exception("File %s not found" % path)
    parsed_data = {}
    with open(filepath, "r") as f_in:
        filelines = f_in.readlines()
        for line in filelines:
            data_values = line.strip().split(",")
            parsed_data[data_values[DISH_ID_INDEX]] = data_values
    return parsed_data


def ReadIdCafe(filepath: str = "dish_ids_cafe1.txt"):
    with open(filepath) as file:
        dish_ids_cafe = file.readlines()
        dish_ids_cafe = [dish.strip() for dish in dish_ids_cafe]
        return dish_ids_cafe


def extract_dish_data(dish: list):
    # Extract first 6th elements in 'dish'
    dish_id, calories, mass, fat, carb, protein = dish[:6]
    # Starting from the 7th element, group elements by 3 continuously
    ingrs = [dish[6:][i : i + 7] for i in range(0, len(dish[6:]), 7)]
    # Reformat ingrs into an object format
    ingrs = [
        {
            "ingr_id": x[0],
            "ingr_name": x[1],
            "mass": x[2],
            "calories": x[3],
            "fat": x[4],
            "carb": x[5],
            "protein": x[6],
        }
        for x in ingrs
    ]
    return {
        "dish_id": dish_id,
        "calories": calories,
        "mass": mass,
        "fat": fat,
        "carb": carb,
        "protein": protein,
        "ingrs": ingrs,
    }


dish_metadata_cafe1 = ReadCsvData(
    __dir__ / "resources" / "dish_metadata_cafe1.csv"
)  # calories food
dish_metadata_cafe2 = ReadCsvData(
    __dir__ / "resources" / "dish_metadata_cafe2.csv"
)  # no calories food
dish_ids_cafe1 = ReadIdCafe(__dir__ / "resources" / "dish_ids_cafe1.txt")
# dish_ids_cafe2 = ReadIdCafe("dish_ids_cafe2.txt")
