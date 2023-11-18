number_count=0
sum=0
input_number=float(input("Enter a number:"))
if input_number==0:
    print("Error: First value cannot be 0")
    exit()
while input_number!=0:
    sum += input_number
    number_count+=1
   
    input_number=float(input("Enter a number:"))

print("The average is:",sum/number_count)