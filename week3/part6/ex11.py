from functools import reduce

def multiply_all(data):
    return reduce(lambda x, y: x * y, data)

print("11. multiply_all:", multiply_all([2, 3, 4]))  # → 24
