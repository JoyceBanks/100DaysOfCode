import requests
import os
from datetime import datetime

APP_ID = os.environ['APP_ID']
API_KEY = os.environ['API_KEY']
EXERCISE_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEET_ENDPOINT = os.environ['SHEET_ENDPOINT']
USERNAME = os.environ['USERNAME']
PASSWORD = os.environ['PASSWORD']

EXERCISE_INPUT = input("Tell me which exercises you did: ")
GENDER = "female"
WEIGHT = 52
HEIGHT = 1148.5
AGE = 23
today = datetime.now()
DATE = today.strftime("%d/%m/%Y")
TIME = today.strftime("%X")

header = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

exercise_params = {
    "query": EXERCISE_INPUT,
    "gender": GENDER,
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE,
}

exercise_response = requests.post(url=EXERCISE_ENDPOINT, json=exercise_params, headers=header)
exercise_response.raise_for_status()
result = exercise_response.json()

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": DATE,
            "time": TIME,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(SHEET_ENDPOINT, json=sheet_inputs, auth=(USERNAME, PASSWORD))

    print(sheet_response.text)
