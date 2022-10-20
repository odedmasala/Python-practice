import json
import os
import sys

# # Option 1
# data = {}
# data["name"] = "Dana"
# data["address"] = {}
# data["address"]["city"] = "Eilat"

# Option 2
data = {"name": "Dana", "address": {"city": "Eilat"}}

path = os.path.join(sys.path[0], "demo2.json")

with open(path, "w") as f:
    json.dump(data, f)
