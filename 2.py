#Write and test a function that takes an integer as its parameter and returns the
#factors of that integer. (A factor is an integer which can be multiplied by another to
#yield the original).

def find_factors(n):
    factors = []
    for i in range(1, n + 1):
        if n % i == 0:
            factors.append(i)
    return factors

# Example usage:
number = 12
result = find_factors(number)
print(f"The factors of {number} are: {result}")


