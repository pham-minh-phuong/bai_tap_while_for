import random

def main():
    max_value = random.randint(1, 100)
    updates = 0

    print(f"Initial maximum value: {max_value}")

    for _ in range(99):
        new_int = random.randint(1, 100)
        if new_int > max_value:
            updates += 1
            max_value = new_int
            print(f"{new_int} (New Maximum)")
        else:
            print(new_int)

    print(f"Maximum value encountered: {max_value}")
    print(f"Number of updates to maximum value: {updates}")

if __name__ == "__main__":
    main()
