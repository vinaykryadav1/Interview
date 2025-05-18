import requests
import random


# url = ["https://ron-swanson-quotes.herokuapp.com/v2/quotes","https://api.adviceslip.com/advice",
#        "https://api.quotable.io/random","http://numbersapi.com/random/trivia?json",
#        "http://api.forismatic.com/api/1.0/?method=getQuote&lang=en&format=json"]


url = "https://zenquotes.io/api/random"

response = requests.get(url)

response.raise_for_status()

data = response.json()[0]["q"]

print(data)
