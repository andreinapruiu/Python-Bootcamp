def remove_negatives(data):
    return list(filter(lambda x: x >= 0, data))

print("10. remove_negatives:", remove_negatives([-2, 0, 3, -1, 7]))  # → [0, 3, 7]
