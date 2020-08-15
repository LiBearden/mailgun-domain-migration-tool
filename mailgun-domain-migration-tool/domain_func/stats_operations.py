# Function to retrieve stats from the source domain
import requests


def get_stats(self, name, region):
    r = requests.get(
        f"{BASE_URL}/{SRC_DOMAIN_NAME}/stats/total",
        auth=("api", SOURCE_API),
        params={"event": ["accepted", "delivered", "failed"],
                "duration": "90d"})
    with open(f"90_day_stats_{SRC_DOMAIN_NAME}.json", "w") as write_file:
        json.dump(r, write_file, indent=4)