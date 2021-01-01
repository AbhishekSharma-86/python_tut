l=[]
i=int(input("Enter the size of the list"))
s=0

for x in range(0,i):
    y=int(input("Enter the elements in the list:"))
    l.append(y)
    s=s+l[x]
    x+=1


print(s)


