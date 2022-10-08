"""
Command: prime_numbers
Return a list of all the prime numbers inferior or equal to n
"""
import math


def prime_numbers(n):

    result = [2]
    for i in range(3, n+1):
        for nombre_premier_precedent in result:
            if i % nombre_premier_precedent == 0 and nombre_premier_precedent < math.sqrt(i):
                return False
            else:
                result.append(i)
        return True
    return result


"""
Command: sum_prime_numbers
Return a sum of all the prime numbers inferior or equal to n
"""
def sum_prime_numbers(n):
    return sum(prime_numbers(n))
