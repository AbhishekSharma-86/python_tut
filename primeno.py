x=int(input("Enter a number:"))
z=0

for y in range(2,x):
    if x%y==0:
        z=1
if z==0:
    print("prime")
else:
    print("not prime")

    

