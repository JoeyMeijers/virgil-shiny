import random

data = {
    "Christine Neal": 8959.15884,
    "Brian Wilson": 8053.16200,
    "Robert Baker": 4640.96400,
    "Elijah White": 4307.15100,
    "Michael Bryan": 3686.84958,
    "Abigail Jones": 3285.28000,
    "Richard Vargas": 2972.21000,
    "Johnathan Miller": 2172.65300,
    "Jennifer Gibson": 2126.24000,
    "Melissa Burke": 2103.44973,
    "Mrs. Gina Silva": 2032.57000,
    "Norma Davis": 1829.68500,
    "Andrew Cruz": 1759.88000,
    "Brenda Grant": 1666.21500,
    "Laura Harper": 1595.72000,
    "Chad Owen": 1315.78500
}

adjusted_data = {}
for key, value in data.items():
    # Generate a random adjustment percentage between 5% and 20%
    adjustment_percentage = random.uniform(5, 20)
    
    # Decide whether to add or subtract based on a random choice
    if random.choice([True, False]):
        adjusted_value = value + (value * (adjustment_percentage / 100))
    else:
        adjusted_value = value - (value * (adjustment_percentage / 100))
    
    adjusted_data[key] = adjusted_value

MAX_VOORRAAD = adjusted_data