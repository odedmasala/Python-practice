from functools import reduce

li = [6, 2, 8, 12, 4,1]

print(reduce(lambda x,y: x if x < y else y,li))
