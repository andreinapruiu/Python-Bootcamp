def is_prime(num):
    if num < 2:
        return False
    return all(num % i != 0 for i in range(2, int(num**0.5) + 1))

def get_primes_up_to(n):
    return [i for i in range(n + 1) if is_prime(i)]

n = int(input("Enter a number: "))
print("Prime numbers:", get_primes_up_to(n))
