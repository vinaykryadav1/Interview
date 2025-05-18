import requests
import smtplib
import time
import random

email = "vinaykryadav2002@gmail.com" 
password = "rrwp pwqe uyej jima"
url = ["https://zenquotes.io/api/random",
    "https://ron-swanson-quotes.herokuapp.com/v2/quotes",
    "https://api.adviceslip.com/advice",
    "https://api.quotable.io/random",
    "http://numbersapi.com/random/trivia?json",
    "http://api.forismatic.com/api/1.0/?method=getQuote&lang=en&format=json"
    ]


for _ in range(2):
    url = random.choice(url)

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()[0]["q"]

    except Exception as e:
        print(f"Error fetching quote: {e}")

#  Email Send
    try:
        connect = smtplib.SMTP("smtp.gmail.com")
        connect.starttls()
        connect.login(email, password)
        connect.sendmail(
            from_addr=email,
            to_addrs=email,
            msg=f"Subject: Daily_Quotes\n\n{data}"
        )
        print("Email sent successfully.")
        connect.quit()
        time.sleep(10)
    except Exception as e:
        print(f"Error: {e}")
        break

