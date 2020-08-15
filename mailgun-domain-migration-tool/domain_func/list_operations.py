# Function to retrieve mailing lists from the source domain
import requests
import config


def get_lists(self):
    r_lists = requests.get(
        f"{BASE_US}/lists/pages",
        auth=('api', 'YOUR_API_KEY'))
    list_mem = []
    for list_item in r_lists["items"]:
        pass