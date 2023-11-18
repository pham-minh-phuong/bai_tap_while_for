n=-1
while (n<0):
    n=int(input("Enter a decimal number(n>0):"))
x=n
ket_qua=""
while (n>0):
    ket_qua= str(n%2)+ket_qua
    n=n//2
print("Kết quả",ket_qua)
    
