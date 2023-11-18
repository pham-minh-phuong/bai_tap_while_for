def calculate_admission_cost(ages):
    total_cost = 0
    for age in ages:
        if age <= 2:
            cost = 0
        elif 3 <= age <= 12:
            cost = 14.00
        elif 65 <= age:
            cost = 18.00
        else:
            cost = 23.00
        total_cost += cost
    return total_cost

def main():
    ages = []
    while True:
        age = input("Enter age: ")
        if age == "":
            break
        try:
            age = int(age)
        except ValueError:
            print("Invalid age:", age)
            continue
        ages.append(age)
    total_cost = calculate_admission_cost(ages)
    print("Total admission cost:", "{:.2f}".format(total_cost))

if __name__ == "__main__":
    main()
