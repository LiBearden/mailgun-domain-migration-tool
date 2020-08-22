# Function to retrieve routes from the source account
import requests
import json
from config import config


def get_add_routes(src_api, dest_api, src_url, dest_url, src_domain):
    routes_list = []
    response = requests.get(
        f"{src_url}/routes",
        auth=("api", src_api),
        params={"skip": 0, "limit": 100})
    routes = json.loads(response)
    for route in routes["items"]:
        if src_domain in route["items"]["expression"]:
            routes_list.append(route)

    # Define functionality to add retrieved routes to destination
    for route in routes_list:
        route_desc = route["items"]["description"]
        route_express = route["items"]["expression"]
        route_priority = route["items"]["priority"]
        route_action = route["items"]["actions"]
        create_resp = requests.post(
            f"{dest_url}/routes",
            auth=("api", dest_api),
            data={"priority": route_priority,
                  "description": route_desc,
                  "expression": route_express,
                  "action": route_action})
        if create_resp.status_code == 200:
            print("All routes added to destination account successfully!")
        else:
            print("Something went wrong. :(")