def compute_parity_bit(data):
    if len(data) != 8:
        raise ValueError("Invalid input: Expected 8 bits")
    num_ones = data.count('1')
    if num_ones % 2 == 0:
        parity_bit = '0'
    else:
        parity_bit = '1'
    return parity_bit

def main():
    while True:
        data = input("Enter 8 bits: ")
        if data == "":
            break
        try:
            parity_bit = compute_parity_bit(data)
        except ValueError as e:
            print(e)
            continue
        print("Parity bit:", parity_bit)

if __name__ == "__main__":
    main()
