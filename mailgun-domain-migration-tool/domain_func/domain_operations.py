import requests


class Domain:

    # Initiate class constructor
    def __init__(self, api, url, name, region):
        self.api = api
        self.url = url
        self.name = name
        self.region = region

    # Function to retrieve domain info, with conditional logic based on region
    def get(self):
        r = requests.get(
            f"{self.url}/domains",
            auth=("api", self.api),
            data={'name': self.name})
        return r

    # Function to add domain to destination account/region
    def add(self):
        r = requests.post(
            f"{self.url}/domains",
            auth=("api", self.api),
            data={'name': self.name})
        return r

    # Function to delete domain from source account/region
    def delete(self):
        r = requests.delete(
            f"{self.url}/domains",
            auth=("api", self.api),
            data={'name': self.name})
        return r