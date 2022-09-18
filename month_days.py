mv=int(input("Enter the month value:"))
list1=(1,3,5,7,8,10,12)
list2=(4,6,9,11)
if mv in list1:
       print("The month has 31days")
elif mv in list2:
    print("The month has 30 days")
elif mv==2:
    print("The month has 28/29 days")
else:
    print("Wrong input")
