import random

while True:
    value = random.randint(0, 25)
    print("Generated:", value)
    if value % 7 == 0 and value != 0:
        print("Found a multiple of 7:", value)
        break
