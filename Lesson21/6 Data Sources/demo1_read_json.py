import json
import os
import sys

# Mode: 'r' - Read
#       'w' - Write
#       'a' - Append

path = os.path.join(sys.path[0], "demo1.json")

# # Option 1
# f = open(path, "r")
# data = json.load(f)
# f.close()

# Option 2
with open(path, "r") as f:
    data = json.load(f)
# The 'with' will close the file automatically when done

print(data)
