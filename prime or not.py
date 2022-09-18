n=int(input("Enter the number "))
c=1
for i in range(2,n):
    if n%i==0:
        c=0
if c==1:
    print("Number is prime")
else:
    print("Number is not prime")
