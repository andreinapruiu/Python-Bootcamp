import sys

print("5. Comprehension vs Generator Memory Usage (cubes 1 to 10):")

cube_list = [x**3 for x in range(1, 11)]
cube_gen = (x**3 for x in range(1, 11))

print("List comprehension size:", sys.getsizeof(cube_list))
print("Generator expression size:", sys.getsizeof(cube_gen))