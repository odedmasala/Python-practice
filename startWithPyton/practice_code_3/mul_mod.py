from add_mod import add


def max(num1, num2):
    max_sum = 0
    for i in range(num2):
            max_sum = add(max_sum, num1)
    return max_sum


print(max(5, 5))
