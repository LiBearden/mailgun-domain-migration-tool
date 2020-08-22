import requests
import json

"""
Well... here, we need to make sure we call all lists from the account in a given region, but only save the
ones that are relevant to the source domain.

Next, we have to retrieve from that saved file only the lists that match the source domain, and then add them
to the destination domain (along with their respective members).
"""


# Function to retrieve mailing lists from the source domain
def get_lists(api, name, url):
    r_lists = requests.get(
        f"{url}/lists/pages",
        auth=('api', api))
    list_mem = []
    for list_item in r_lists["items"]:
        members = requests.get(f"https://{url}/v3/lists/{list_item}/members/pages",
        auth=('api', api))

        with open(f"list_members_{name}.json", "w") as write_file:
            json.dump(members, write_file, indent=4)
        print(f"lists referring to {name} successfully saved!")


# Function to add mailing lists from source domain to destination domain
def add_list_member(api, name, url):
    with open(f"list_members_{name}.json", "r") as read_file:
        json.loads(read_file, indent=4)

    for item in read_file:
        address = item["address"]
        return requests.post(f"https://{url}/v3/lists/{address}/members.json",
                             auth=('api', api),
                             data={'upsert': True,
                                   'members': item})