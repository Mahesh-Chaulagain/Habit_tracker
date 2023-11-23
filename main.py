import requests
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

USERNAME = os.getenv("USERNAME")
TOKEN = os.getenv("TOKEN")
GRAPH_ID = os.getenv("GRAPH_ID")

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
#
# graph_params = {
#     "id": "GRAPH_ID",
#     "name": "Coding Graph",
#     "unit": "minute",
#     "type": "float",
#     "color": "shibafu",
# }
#
headers = {
    "X-USER-TOKEN": TOKEN,
}
#
# response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
# print(response.text)

# Step 3. get the graph
# https://pixe.la/v1/users/maheshc/graphs/graph1.html

# Step 4. post value to the graph
pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

pixel_data = {
    "date": "20231123",
    "quantity": "90.0",
}

response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
print(response.text)
