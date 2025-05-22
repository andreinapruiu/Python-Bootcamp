def median_of_three_or_more(*args):
    if len(args) < 3:
        return "Need at least three numbers"
    sorted_nums = sorted(args)
    mid = len(sorted_nums) // 2
    return sorted_nums[mid] if len(args) % 2 != 0 else (sorted_nums[mid - 1] + sorted_nums[mid]) / 2

print("6. median (odd):", median_of_three_or_more(1, 9, 3))     # → 3
print("6. median (even):", median_of_three_or_more(2, 4, 6, 8)) # → (4+6)/2 = 5.0
