# variables convention: snake_case
def get_len(str="Hello"):
    return len(str)


def get_arr_total_len(li):
    total = 0
    for string in li:
        total += get_len(string)
    return total

total = get_arr_total_len(["hi", "bye", "hello"])
print(total)