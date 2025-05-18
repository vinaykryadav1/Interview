import requests

APP_ID = "e087d3c"
API_KEY = "ac32b79b2e483d4d1d48ddf9a41ddbc"

# API endpoint
url = "https://trackapi.nutritionix.com/v2/natural/nutrients"

# User input
exercise_text = input("Tell me what you ate: ")

# Headers
headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "Content-Type": "application/json"
}

# JSON data to send in body
body = {
    "query": exercise_text
}

# Sending POST request
response = requests.post(url=url, json=body, headers=headers)

# Handle the response
data = response.json()["foods"]

item = data[0]["food_name"]
calories =  data[0]["nf_calories"]
total_fat = data[0]["nf_total_fat"]
cholesterol = data[0]["nf_cholesterol"]
sodium = data[0]["nf_sodium"]
total_carbohydrate = data[0]["nf_total_carbohydrate"]
sugar = data[0]["nf_sugars"]
protein = data[0]["nf_protein"]
potassium = data[0]["nf_potassium"]


values_list = [item, calories, total_fat, cholesterol, sodium, total_carbohydrate, sugar, protein, potassium]
keys = ["item", "calories", "total_fat", "cholesterol", "sodium", "total_carbohydrate", "sugar", "protein", "potassium"]
nutrition_dict = dict(zip(keys, values_list))

print(nutrition_dict)
