import requests

path = "https://api.kodim.cz/python-data/people"

response = requests.get(path)
print(response) # i have reached the address, you may continue

data = response.json()
# print(data)

print(data[0]["first_name"])
print(f"There are in total {len(data)} people on the list")

print("The following sections are on the list:")
for key, value in data[0].items():
    print(key)
    # for key, value in item.items():

print(data[0].keys())

female = 0
male = 0
    
for item in data:
    if item["gender"] == "Male":
        male += 1
    elif item["gender"] == "Female":
        female += 1

print(f"We have {female} females on the list and {male} males.")
