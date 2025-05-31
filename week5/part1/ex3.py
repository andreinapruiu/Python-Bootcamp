import math

def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

def generate_primes(n):
    for num in range(2, n):
        if is_prime(num):
            yield num

print("3. Prime Number Generator:")
print(list(generate_primes(30)))