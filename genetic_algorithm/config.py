class MealProgram:
    diet = "low"  # @param ["low", "balanced", "abundant"]
    calo = "1500"  # @param [1500, 2000, 2500]
    gender = "male"  # @param ["male", "female"]
    age = 20  # @param {type:"number"}
    calo = int(calo)
    fat = {  # unit (g)
        "low-1500": 50,
        "low-2000": 67,
        "low-2500": 83,
        "abundant-1500": [83, 125],
        "abundant-2000": [111, 167],
        "abundant-2500": [139, 208],
    }.get(diet + "-" + str(calo))

    carb = {"male": 34, "female": 24}.get(gender)  # unit (g)

    protein = {"male": 52, "female": 45}.get(gender)  # unit (g)


class ObjectiveConstraint:
    meal_program = MealProgram()
    error_rate = 0.1


constraint = ObjectiveConstraint()

# Example usage (replace objective function with your specific problem)
chromosome_length = 21
generations = 100
population_size = 50
crossover_rate = 0.8
mutation_rate = 0.2
