#!/usr/bin/env python3.7

# -*- coding: utf-8 -*-

# Created by Elliot "Li" Bearden
# Aug. 14th, 2020

import domain_func
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

Q_MIGRATION = config["migration_type"]["quick_migration"].lower()
F_MIGRATION = config["migration_type"]["full_migration"].lower()


def src_region():
    if SOURCE_REGION == 'us':
        src_url = BASE_US
        return src_url
    elif SOURCE_REGION == 'eu':
        src_url = BASE_EU
        return src_url
    else:
        print("Sorry, you have entered an invalid source region. Please check your configuration and try again.")


def dest_region():
    if DESTINATION_REGION == 'us':
        dest_url = BASE_US
        return dest_url
    elif DESTINATION_REGION == 'eu':
        dest_url = BASE_EU
        return dest_url
    else:
        print("Sorry, you have entered an invalid region. Please check your configuration and try again.")


src_region()
dest_region()

s = Domain(SOURCE_API, base_url, SRC_DOMAIN_NAME, SOURCE_REGION)
d = Domain(DESTINATION_API, base_url, DEST_DOMAIN_NAME, DESTINATION_REGION)

if Q_MIGRATION == "yes":
    s.delete()
    d.add()
elif F_MIGRATION == "yes":
    domain_func.get_add_routes(SOURCE_API, DESTINATION_API, src_url, dest_url, SRC_DOMAIN_NAME)
    domain_func.get_stats(SOURCE_API, SRC_DOMAIN_NAME, src_url)
    domain_func.get_events(SOURCE_API, SRC_DOMAIN_NAME, src_url)
    s.delete()
    d.add()
else:
    print("Sorry, it appears that the migration type was not specified. Please check the config.py file for errors.")

print("Migration complete! Check your control panel for domain verification details.")
