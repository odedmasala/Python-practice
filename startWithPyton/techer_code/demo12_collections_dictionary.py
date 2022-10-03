col = {1: "Avi", 5: "Dana", 7: "Ron", "AA": 100}

print(col)

# Get the value by his keys
print(col[5])
print(col["AA"])

# Replace existing value with a new one
col[5] = "Aviva"
print(col)


# Add new key-value pair
col[10] = "Dolev"
print(col)

keys = list(col.keys())

print(keys)


if 5 in keys:
    print("Exist")

# Get all values
vals = list(col.values())
print(vals)


if "Aviva" in vals:
    print("Aviva Exist")
