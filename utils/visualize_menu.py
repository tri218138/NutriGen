from typing import List
from utils.helper_function import dish_metadata_cafe1, extract_dish_data
from datasets import load_dataset


# nutrition5k_ds = load_dataset("TeeA/nutrition5k-food-name-gemini", "resources/")


def get_dish_repo_by_dish_id(dish_id: str):
    return {"food_name": "ABC", "dish_image": None}
    dish = nutrition5k_ds.filter(dish_id=dish_id)
    if len(dish) > 0:
        return dish
    return {}


def get_dishes_data_from_individual(individual):
    result_dishes = [dish_metadata_cafe1[id] for id in individual]
    result_dishes = [extract_dish_data(dish) for dish in result_dishes]
    return result_dishes


def render_nutritious_week(dishes: List):
    if isinstance(dishes[0], str):
        dishes = get_dishes_data_from_individual(dishes)
    assert (
        len(dishes) == 21
    ), "The 'dishes' list must contain exactly 21 dishes: a week with 3 meal a day"

    # Define icons for morning, lunch, and afternoon
    sessions_of_day = [r"$\odot$", r"$\clubsuit$", r"$\bigstar$"]
    sessions_of_day = ["☀️", "🍽️", "🌅"]
    sessions_of_day = ["Morning", "Lunch", "Afternoon", "Nightly"]
    days_of_week = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday",
    ]

    result = {}

    for day in range(7):

        total_calo = {"fat": 0.0, "carb": 0.0, "protein": 0.0}
        result[days_of_week[day]] = {}

        for j in range(3):
            dish_index = day * 3 + j
            dish = dishes[dish_index]

            for factor in total_calo:
                total_calo[factor] += float(dish[factor])
            dish["total_calories"] = total_calo
            ### Add food_name and dish_image
            for key, value in get_dish_repo_by_dish_id(dish["dish_id"]).items():
                dish[key] = value

            result[days_of_week[day]][sessions_of_day[j]] = dish
    return result


if __name__ == "__main__":
    best_individual = [
        "dish_1550777566",
        "dish_1568233509",
        "dish_1551492590",
        "dish_1551390651",
        "dish_1566245437",
        "dish_1558723414",
        "dish_1559238993",
        "dish_1565383026",
        "dish_1550779058",
        "dish_1559678083",
        "dish_1561577177",
        "dish_1550774815",
        "dish_1565117962",
        "dish_1567628193",
        "dish_1563568357",
        "dish_1559332795",
        "dish_1566934152",
        "dish_1551235240",
        "dish_1556575446",
        "dish_1560453294",
        "dish_1565379827",
    ]

    # Call the function with your list of dishes
    render_nutritious_week(best_individual)
