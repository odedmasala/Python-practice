arr = [6,3,8,1,7]

#option 1
# arr2 = []
# for num in arr:
#     arr2.append(num*2)

# Option 2


arr2 = list(map(lambda num: num * 2,arr))
print(arr2)