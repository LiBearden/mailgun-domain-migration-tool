# Function to retrieve events from the source domain
import requests


def get_events(self, name, region):
    r = requests.get(
        f"{BASE_URL}/{SRC_DOMAIN_NAME}/events",
        auth=("api", SOURCE_API),
        params={"begin": datetime.now() - timedelta(hours=72),
                "ascending": "yes",
                "limit": 100,
                "pretty": "yes",
                "event": "accepted OR delivered OR failed"})
    with open(f"72_hr_events{SRC_DOMAIN_NAME}.json", "w") as write_file:
        json.dump(r, write_file)