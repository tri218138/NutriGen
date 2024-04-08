from flask import Flask, request, jsonify
import time
from genetic_algorithm.gen_algo import genetic_algorithm
from genetic_algorithm.config import (
    chromosome_length,
    generations,
    population_size,
    crossover_rate,
    mutation_rate,
)
from datasets import load_dataset
from utils.nutrition5k_repo import repo
from utils.visualize_menu import render_nutritious_week


app = Flask(__name__)


@app.route("/", methods=["GET"])
def get_homepage():
    return (
        jsonify(
            {"message": "Hello friend!\n Please redirect to \\recommend with POST data"}
        ),
        200,
    )


# Define API endpoints
@app.route("/user", methods=["POST"])
def get_user_data():
    user_data = request.json  # Assuming user data is sent as JSON
    # Process user data and store it or use it directly for recommendation
    return jsonify({"message": "User data received successfully"}), 200


@app.route("/recommend", methods=["POST", "GET"])
def recommend_food(user_data: dict = None):
    start_time = time.time()  # Record start time

    user_data = user_data if not None else request.json

    # Use your ML model to generate food recommendations based on user data
    with app.app_context():
        best_individual, best_fitness = genetic_algorithm(
            population_size,
            chromosome_length,
            generations,
            crossover_rate,
            mutation_rate,
        )

    end_time = time.time()  # Record end time
    response_time = end_time - start_time  # Calculate response time

    print("Best Individual:", best_individual)
    print("Best Fitness:", best_fitness)
    print("Response Time:", response_time)
    print(render_nutritious_week(best_individual))

    return (
        jsonify(
            {
                "best_individual": best_individual,
                "best_fitness": best_fitness,
                "response_time": response_time,
                "dish_metadata": render_nutritious_week(best_individual),
            }
        ),
        200,
    )


if __name__ == "__main__":
    # recommend_food(
    #     {
    #         "age": 18,
    #         "gender": "male",
    #     }
    # )
    print("Downloading Nutrition5k dataset (2.54GB)")
    # nutrition5k_ds = load_dataset(
    #     repo,
    # )
    # Save the dataset to your directory
    # nutrition5k_ds.save_to_disk("resources/")
    app.run("0.0.0.0", debug=True)
