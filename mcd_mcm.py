from math import gcd
from functools import reduce
from collections import Counter

def prime_factors(n):
    """Obtiene los factores primos de un número."""
    i = 2
    factors = []
    while i * i <= n:
        while (n % i) == 0:
            factors.append(i)
            n //= i
        i += 1
    if n > 1:
        factors.append(n)
    return factors

def lcm(a, b):
    """Calcula el MCM de dos números usando el MCD."""
    return abs(a * b) // gcd(a, b)

def lcm_multiple(numbers):
    """Calcula el MCM de una lista de números."""
    return reduce(lcm, numbers)

def gcd_multiple(numbers):
    """Calcula el MCD de una lista de números."""
    return reduce(gcd, numbers)

def mcm_factorization(numbers):
    """Calcula el MCM usando descomposición factorial."""
    all_factors = Counter()
    for n in numbers:
        factor_counts = Counter(prime_factors(n))
        for prime, count in factor_counts.items():
            all_factors[prime] = max(all_factors[prime], count)
    mcm = 1
    for prime, count in all_factors.items():
        mcm *= prime ** count
    return mcm

def mcd_factorization(numbers):
    """Calcula el MCD usando descomposición factorial."""
    common_factors = Counter(prime_factors(numbers[0]))
    for n in numbers[1:]:
        factor_counts = Counter(prime_factors(n))
        common_factors &= factor_counts
    mcd = 1
    for prime, count in common_factors.items():
        mcd *= prime ** count
    return mcd

# Interfaz principal
def main():
    print("Programa para calcular el MCM y MCD de tres o más números.")
    numbers = list(map(int, input("Ingresa los números separados por espacios: ").split()))
    
    if len(numbers) < 3:
        print("Por favor, ingresa al menos tres números.")
        return

    # Método 1: Descomposición factorial
    print("\nMétodo 1: Descomposición factorial")
    mcd_fact = mcd_factorization(numbers)
    mcm_fact = mcm_factorization(numbers)
    print(f"MCD (descomposición factorial): {mcd_fact}")
    print(f"MCM (descomposición factorial): {mcm_fact}")

    # Método 2: Algoritmo de Euclides
    print("\nMétodo 2: Algoritmo de Euclides")
    mcd_euclides = gcd_multiple(numbers)
    mcm_euclides = lcm_multiple(numbers)
    print(f"MCD (Euclides): {mcd_euclides}")
    print(f"MCM (Euclides): {mcm_euclides}")

if __name__ == "__main__":
    main()
