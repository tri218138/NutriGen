import random
from tqdm import tqdm
from genetic_algorithm.config import (
    chromosome_length,
    generations,
    population_size,
    crossover_rate,
    mutation_rate,
    constraint,
)
from utils.helper_function import (
    dish_metadata_cafe1,
    dish_metadata_cafe2,
    dish_ids_cafe1,
)

random.seed(42)


def calculate_total_calory(individual, factor: str = "all"):
    assert factor in ["all", "fat", "carb", "protein"]
    index = {"all": 1, "fat": 3, "carb": 4, "protein": 5}.get(factor)
    calories = [dish_metadata_cafe1[dish][index] for dish in individual]
    return sum(float(calo) for calo in calories)


def objective_function(individual, constraint: object = None):
    # Target is maximize objective_function
    # For each breach of constraints, minus 1 point
    # Return fitness in range (0,1]
    min_calo_a_day_target = constraint.meal_program.calo * (1 - constraint.error_rate)
    max_calo_a_day_target = constraint.meal_program.calo * (1 + constraint.error_rate)
    min_carb_a_day_target = constraint.meal_program.carb * (1 - constraint.error_rate)
    max_carb_a_day_target = constraint.meal_program.carb * (1 + constraint.error_rate)
    min_protein_a_day_target = constraint.meal_program.protein * (
        1 - constraint.error_rate
    )
    max_protein_a_day_target = constraint.meal_program.protein * (
        1 + constraint.error_rate
    )
    if type(constraint.meal_program.fat) is list:
        min_fat_a_day_target, max_fat_a_day_target = constraint.meal_program.fat
    else:
        min_fat_a_day_target = constraint.meal_program.fat * (1 - constraint.error_rate)
        max_fat_a_day_target = constraint.meal_program.fat * (1 + constraint.error_rate)

    # print(min_calo_a_day_target, max_calo_a_day_target)
    # print(min_carb_a_day_target, max_carb_a_day_target)
    # print(min_protein_a_day_target, max_protein_a_day_target)
    # print(min_fat_a_day_target, max_fat_a_day_target)

    ### Init fitness
    # 10 point for a day error and 10 for a whole week error
    max_fitness = 72
    fitness = max_fitness

    ### For a week
    if len(set(individual)) < 21:
        fitness -= 2

    ### For a day
    for day in range(7):
        dishes_a_day = individual[day * 3 : day * 3 + 3]
        morning, lunch, afternoon = dishes_a_day
        # If it get duplicated, no point
        if len(set(dishes_a_day)) < 3:
            fitness -= 1
        # Calculate calo a day, must in range
        calo_a_day = calculate_total_calory(dishes_a_day)
        if not min_calo_a_day_target < calo_a_day < max_calo_a_day_target:
            fitness -= 3
        # The lunch contains the most calories
        if max(dishes_a_day) != lunch:
            fitness -= 1
        # Balance fat, carb, protein
        fat_a_day = calculate_total_calory(dishes_a_day, factor="fat")
        if not min_fat_a_day_target < fat_a_day < max_fat_a_day_target:
            fitness -= 2
        carb_a_day = calculate_total_calory(dishes_a_day, factor="carb")
        if not min_carb_a_day_target < carb_a_day < max_carb_a_day_target:
            fitness -= 2
        protein_a_day = calculate_total_calory(dishes_a_day, factor="protein")
        if not min_protein_a_day_target < protein_a_day < max_protein_a_day_target:
            fitness -= 2

    return max(fitness, 0) / max_fitness


def create_individual(chromosome_length):
    # Create a random individual (chromosome)
    return [
        dish_ids_cafe1[random.randint(0, len(dish_ids_cafe1) - 1)]
        for _ in range(chromosome_length)
    ]


def create_population(population_size, chromosome_length):
    # Create a population of random individuals
    population = []
    for _ in range(population_size):
        population.append(create_individual(chromosome_length))
    return population


def selection(population, fitness_scores):
    # Selection function (e.g., Roulette Wheel Selection)
    # Select two parents based on their fitness scores
    # You can implement different selection methods here
    return random.choices(population, weights=fitness_scores, k=2)


def crossover(parent1, parent2, crossover_rate):
    # Crossover function (e.g., Single-point crossover)
    # With a probability (crossover_rate), swap genes between parents
    if random.random() < crossover_rate:
        crossover_point = random.randint(1, len(parent1) - 1)
        offspring1 = parent1[:crossover_point] + parent2[crossover_point:]
        offspring2 = parent2[:crossover_point] + parent1[crossover_point:]
    else:
        offspring1 = parent1
        offspring2 = parent2
    return offspring1, offspring2


def mutation(individual, mutation_rate):
    # Mutation function (e.g., Bit flip mutation)
    # With a probability (mutation_rate), flip a random gene
    for i in range(len(individual)):
        if random.random() < mutation_rate:
            individual[i] = dish_ids_cafe1[
                random.randint(0, len(dish_ids_cafe1) - 1)
            ]  # Flip gene value (e.g., 0 to 1 or vice versa)
    return individual


def genetic_algorithm(
    population_size, chromosome_length, generations, crossover_rate, mutation_rate
):
    global constraint
    # Main GA loop
    population = create_population(population_size, chromosome_length)
    for idx, _ in tqdm(enumerate(range(generations)), desc=f"Generation:..."):
        # Evaluate fitness
        fitness_scores = [
            objective_function(individual, constraint) for individual in population
        ]

        # Selection
        parents = selection(population, fitness_scores)

        # Crossover
        offspring1, offspring2 = crossover(parents[0], parents[1], crossover_rate)

        # Mutation
        offspring1 = mutation(
            offspring1.copy(), mutation_rate
        )  # Copy to avoid modifying parents
        offspring2 = mutation(offspring2.copy(), mutation_rate)

        # Create new population
        new_population = sorted(
            population,
            key=lambda individual: objective_function(individual, constraint),
            reverse=True,
        )
        new_population = (
            new_population[: population_size - 2] + [offspring1] + [offspring2]
        )

        # Replace with next generation
        population = new_population

        # # Log best individual at index 0
        # print(objective_function(new_population[0], constraint), objective_function(new_population[-3], constraint))

    # Find best individual
    best_individual = population[0]
    best_fitness = fitness_scores[0]
    for i in range(1, len(population)):
        if fitness_scores[i] > best_fitness:
            best_individual = population[i]
            best_fitness = fitness_scores[i]

    return best_individual, best_fitness


if __name__ == "__main__":
    best_individual, best_fitness = genetic_algorithm(
        population_size, chromosome_length, generations, crossover_rate, mutation_rate
    )

    print("Best Individual:", best_individual)
    print("Best Fitness:", best_fitness)
