def newton_sqrt(x):
    guess = x / 2
    epsilon = 1e-12 
    while abs(guess * guess - x) > epsilon:
        guess = (guess + x / guess) / 2
    return guess
def main():
    x = float(input("Enter a number to find its square root: "))
    if x < 0:
        print("Please enter a non-negative number.")
    else:
        result = newton_sqrt(x)
        print(f"The square root of {x} is approximately {result:.8f}")
if __name__ == "__main__":
    main()
