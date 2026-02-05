import pandas as pd
import os

# Get absolute path to this file's directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Build absolute path to data file
DATA_PATH = os.path.join(BASE_DIR, "..", "data", "emission_factors.csv")

df = pd.read_csv(DATA_PATH)

def get_factor(category, type_):
    row = df[(df["category"] == category) & (df["type"] == type_)]
    return row["factor"].values[0]

def calculate_vehicle_emission(vehicle_type, km):
    return km * get_factor("vehicle", vehicle_type)

def calculate_electricity_emission(kwh):
    return kwh * get_factor("electricity", "india_kwh")

def calculate_food_emission(food_type):
    return get_factor("food", food_type)

def calculate_waste_emission(waste_kg):
    return waste_kg * get_factor("waste", "kg")

def calculate_total(inputs):
    vehicle = calculate_vehicle_emission(inputs["vehicle_type"], inputs["vehicle_km"])
    electricity = calculate_electricity_emission(inputs["electricity_kwh"])
    food = calculate_food_emission(inputs["food_type"])
    waste = calculate_waste_emission(inputs["waste_kg"])

    total = vehicle + electricity + food + waste

    return {
        "vehicle": round(vehicle, 2),
        "electricity": round(electricity, 2),
        "food": round(food, 2),
        "waste": round(waste, 2),
        "total": round(total, 2)
    }
