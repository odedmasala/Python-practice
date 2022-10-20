from functools import reduce

names = ["Yoav", "Ron", "Aviva", "Ronen", "Dan", "Galit"]

lengths = list(map(lambda str: len(str),names))
print(lengths)
# const lengths = names.map(str => str.length))

filtered = list(filter(lambda l: l > 4,lengths))
print(filtered)

total = reduce(lambda x,y: x + y, filtered)
print(total)
