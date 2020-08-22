# Function to retrieve stats from the source domain
import requests
import json


def get_stats(api, name, url):
    r = requests.get(
        f"{url}/{name}/stats/total",
        auth=("api", api),
        params={"event": ["accepted", "delivered", "failed"],
                "duration": "90d"})
    with open(f"90_day_stats_{name}.json", "w") as write_file:
        json.dump(r, write_file, indent=4)
    print(f"90-day statistics for {name} successfully saved!")