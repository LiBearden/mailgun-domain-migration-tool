import requests

class Domain:

    # Initiate class constructor
    def __init__(self, name, region):
        self.name = name
        self.region = region

    # Function to retrieve domain info, with conditional logic based on region
    def get(self):
        r = requests.get(
            f"{BASE_URL}/domains",
            auth=("api", SOURCE_API),
            data={'name': SRC_DOMAIN_NAME})
        return r

    # Function to add domain to destination account/region
    def add(self):
        r = requests.post(
            f"{BASE_URL}/domains",
            auth=("api", DESTINATION_API),
            data={'name': DEST_DOMAIN_NAME})
        return r

    # Function to delete domain from source account/region
    def delete(self):
        r = requests.delete(
            f"{BASE_URL}/domains",
            auth=("api", SOURCE_API),
            data={'name': SRC_DOMAIN_NAME})
        return r