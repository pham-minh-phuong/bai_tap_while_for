import math

def approximate_pi(terms):
    result = 0.0
    for i in range(terms):
        result += ((-1) ** i) / (2 * i + 1)
        print(f"Approximation after {i+1} term(s): {4 * result}")


num_terms = 15


approximate_pi(num_terms)