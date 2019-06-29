"""Uses config setup but with arguments"""
import json
import argparse

PARSER = argparse.ArgumentParser()

REQUIRED = PARSER.add_argument_group('Required arguments')

REQUIRED.add_argument("-apikey", help="Transport API Key", required=True)
ARGS = PARSER.parse_args()


print("Writing auth")

print(ARGS.apikey)

API_KEY = {'api_key': ARGS.apikey}

with open('api_key.json', 'w') as outfile:
    json.dump(API_KEY, outfile)
