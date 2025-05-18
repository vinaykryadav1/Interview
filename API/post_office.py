import requests

pincode = 110045

url = f"https://api.postalpincode.in/pincode/{pincode}"

response = requests.get(url)

response.raise_for_status()

data = response.json()
post_0 = data[0]["PostOffice"][0]

state = post_0["State"]
city = post_0["District"]
post_office = post_0["Name"] 

#print(f" {pincode} :-  State: {state}, City: {city}, Post_Office: {post_office}")
print(state)

