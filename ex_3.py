#Exercise 57 - JSON to Dictionary

import json
from pprint import pprint

with open("smple.json","r") as f:
    d=json.load(f)

pprint(d)