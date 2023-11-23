import requests
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

USERNAME = "maheshc"
TOKEN = os.getenv("TOKEN")
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# Step 1. create user in pixela
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)    # give response back in the form of text

# Step 2. create a new graph in pixela
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

# graph_params = {
#     "id": "GRAPH_ID",
#     "name": "Coding Graph",
#     "unit": "minute",
#     "type": "float",
#     "color": "shibafu",
# }

headers = {
    "X-USER-TOKEN": TOKEN,
}

# response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
# print(response.text)

# Step 3. get the graph
# https://pixe.la/v1/users/maheshc/graphs/graph1.html

# Step 4. post value to the graph
pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()

pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many minutes did you code today?:"),
}

response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
print(response.text)

# Step 5. update value on the graph PUT - /v1/users/<username>/graphs/<graphID>/<yyyyMMdd>
# today = datetime.now()
#
# update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
#
# new_pixel_data = {
#     "quantity": "130.0",
# }
#
# response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
# print(response.text)

# Step 6. delete value in the graph
# today = datetime.now()
#
# delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
#
# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.text)
