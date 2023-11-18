import random
T=0
for i in range(10) :
    S=0
    s=0
    d=0
    while S<3 and s<3:
        n=random.choice(['H','T'])
        print(n,end=" ")
        d+=1
        if n== 'H':
            S+=1
            s=0
        else :
            s+=1
            S=0
    print(f"({d} flips)")
    T+=d
T=float(T)
print(f"On average, {T/10} flips werw needed.")