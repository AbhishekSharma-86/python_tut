num_month=int(input("Enter the number of month:"))
year=int(input("Enter the year:"))
if year%4==0:
    if num_month==2:
        print("the month contains 29 days")
    else:
         if num_month%2==0:
            print("the month contains 30 days")
         else:
            print("The month contains 31 days ")
        
else:
    if num_month==2:
        print("The month contains 28 days")
    elif num_month%2==0:
        print("the month contains 30 days")
    else:
        print("The month contains 31 days ")
y=input("")
