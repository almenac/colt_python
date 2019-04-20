
def max_magnitude(lst):
    return max([abs(x) for x in lst])

foo = [1, 2, 3, -666]

print(max_magnitude(foo))