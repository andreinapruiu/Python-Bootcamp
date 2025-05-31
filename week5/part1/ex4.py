import time

print("4. Lazy Evaluation (sum of squares up to 1 million):")

start_time = time.time()
lazy_sum = sum(x * x for x in range(1_000_000))  # generator expression
print("Generator sum:", lazy_sum)
print("Generator time: %.4f seconds" % (time.time() - start_time))

start_time = time.time()
eager_sum = sum([x * x for x in range(1_000_000)])  # list comprehension
print("List sum:", eager_sum)
print("List time: %.4f seconds" % (time.time() - start_time))
