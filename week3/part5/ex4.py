def is_prime(n):
    if n < 2:
        return False
    return all(n % i != 0 for i in range(2, int(n**0.5) + 1))

limit = int(input("Enter a number: "))
primes = [i for i in range(2, limit) if is_prime(i)]
print("Primes less than", limit, ":", primes)
