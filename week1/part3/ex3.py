set1 = set(range(0, 8))
set2 = set(range(4, 11))

print("All elements from both sets:", set1.union(set2))
print("Common elements from both sets:", set1.intersection(set2))
print("Elements from set1 that are not in set2:", set1.difference(set2))
print("Elements from set2 that are not in set1:", set2.difference(set1))
print("Elements that are in both sets but NOT in common", set1.symmetric_difference(set2))