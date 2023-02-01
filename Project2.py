n=int(input("Enter the number of fibonnaci sequence:"))
n1=0
n2=1

print(n1)
print(n2)
i=2
while i<=n:
    n3=n1+n2
    n1=n2
    n2=n3
    print(n3)
    i+=1
