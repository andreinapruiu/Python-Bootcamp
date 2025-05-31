def custom_range(start, stop, step=1):
    current = start
    while current < stop:
        yield current
        current += step

print("2. Custom Range Generator:")
print(list(custom_range(2, 10, 2)))