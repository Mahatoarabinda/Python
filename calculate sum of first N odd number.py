n=int(input("Enter the number: "))
sum=0
x=1
while x<=n:
    if x%2==1:
        sum=sum+x
    x=x+1
print("Sum of odd number is ",sum)
