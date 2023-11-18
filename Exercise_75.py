def gcd(n, m):
    d = min(n, m)
    while n % d != 0 or m % d != 0:
        d -= 1
    return d
num1 = int(input("Enter first positive integer: "))
num2 = int(input("Enter second positive integer: "))
result = gcd(num1, num2)
print(f"The greatest common divisor of {num1} and {num2} is {result}")
