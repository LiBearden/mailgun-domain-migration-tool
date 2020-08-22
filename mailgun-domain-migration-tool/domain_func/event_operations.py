# Function to retrieve events from the source domain
import requests
import json
from datetime import datetime, timedelta


def get_events(api, name, url):
    r = requests.get(
        f"{url}/{name}/events",
        auth=("api", api),
        params={"begin": datetime.now() - timedelta(hours=72),
                "ascending": "yes",
                "limit": 100,
                "pretty": "yes",
                "event": "accepted OR delivered OR failed"})
    with open(f"72_hr_events{name}.json", "w") as write_file:
        json.dump(r, write_file)