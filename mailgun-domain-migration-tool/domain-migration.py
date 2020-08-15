#!/usr/bin/env python3.7

# -*- coding: utf-8 -*-

# Created by Elliot "Li" Bearden
# Aug. 14th, 2020
import domain_func
import requests
import json
from datetime import datetime, timedelta
from domain_func.domain_operations import Domain
from config import config


SOURCE_API = config["source"]["source_api_key"]
DESTINATION_API = config["destination"]["destination_api_key"]

SOURCE_REGION = config["source"]["source_region"].lower()
DESTINATION_REGION = config["destination"]["destination_region"].lower()

SRC_DOMAIN_NAME = config["source"]["source_domain"]
DEST_DOMAIN_NAME = config["destination"]["destination_domain"]

BASE_US = "https://api.mailgun.net/v3"
BASE_EU = "https://api.eu.mailgun.net/v3"
BASE_URL = ""

Q_MIGRATION = config["migration_type"]["quick_migration"].lower()
F_MIGRATION = config["migration_type"]["full_migration"].lower()


def src_region():
    if SOURCE_REGION == 'us':
        BASE_URL = BASE_US
        return BASE_URL
    elif SOURCE_REGION == 'eu':
        BASE_URL = BASE_EU
        return BASE_URL
    else:
        print("Sorry, you have entered an invalid source region. Please check your configuration and try again.")


def dest_region():
    if DESTINATION_REGION == 'us':
        BASE_URL = BASE_US
        return BASE_URL
    elif DESTINATION_REGION == 'eu':
        BASE_URL = BASE_EU
        return BASE_URL
    else:
        print("Sorry, you have entered an invalid region. Please check your configuration and try again.")


s = Domain(SRC_DOMAIN_NAME, SOURCE_REGION)
d = Domain(DEST_DOMAIN_NAME, DESTINATION_REGION)

if Q_MIGRATION == "yes":
    s.delete()
    d.add()
elif F_MIGRATION == "yes":
    s.get_lists()
    s.get_routes()
    s.get_stats()
    s.get_events()
    s.delete()
    s.add()
else:
    print("Sorry, it appears that the migration type was not specified. Please check the config.py file for errors.")

print("Migration complete! Check your control panel for domain verification details.")
