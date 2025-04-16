my_tuple_1 = (1, 2, 3, "a", "b", 10, "5")
my_tuple_2 = (7, 5, "b", "5", 3)

set_1 = set(my_tuple_1)
set_2 = set(my_tuple_2)

print("Elements from tuple1 that are not in tuple2:", set_1.difference(set_2))

combined = my_tuple_1 + my_tuple_2

print("Combined tuple:", combined)

# Total number of duplicates in the combined tuple
duplicates = len(combined) - len(set(combined))
print("Total number of duplicates in the combined tuple:", duplicates)
