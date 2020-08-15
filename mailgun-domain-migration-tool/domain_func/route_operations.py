# Function to retrieve routes from the source account
import requests
import config


def get_add_routes(self, region, domain=SRC_DOMAIN_NAME):
    routes_list = []
    response = requests.get(
        f"{BASE_URL}/routes",
        auth=("api", SOURCE_API),
        params={"skip": 0, "limit": 100})
    routes = json.loads(response)
    for route in routes["items"]:
        if domain in route["items"]["expression"]:
            routes_list.append(route)

    # Define functionality to add retrieved routes to destination
    for route in routes_list:
        route_desc = route["items"]["description"]
        route_express = route["items"]["expression"]
        route_priority = route["items"]["priority"]
        route_action = route["items"]["actions"]
        create_resp = requests.post(
            f"{BASE_URL}/routes",
            auth=("api", DESTINATION_API),
            data={"priority": route_priority,
                  "description": route_desc,
                  "expression": route_express,
                  "action": route_action})
        if create_resp.status_code == 200:
            print("All routes added to destination account successfully!")
        else:
            print("Something went wrong. :(")