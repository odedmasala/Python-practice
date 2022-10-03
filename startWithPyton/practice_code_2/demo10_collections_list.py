arr = [5, 5, 66, 5, 643, 563]
print(arr)
# Add item to the end of the list

arr.append(5)
arr.append(6)
print(arr)

# Add item to a specific index in the list
arr.insert(1, 10)

print(arr)

# Remove item from the END of the list
arr.pop()
print(arr)

# Remove a specific element from the list (takes one argument - the specific element's value)
arr.remove(5)
print(arr)

# Remove item from the specific index in the list
arr.pop(2)
print(arr)