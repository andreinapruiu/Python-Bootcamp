def average(*args):
    if not args:
        return "No numbers provided."
    return sum(args) / len(args)

print("4. average:", average(4, 6, 8))
print("4. average (no args):", average())
