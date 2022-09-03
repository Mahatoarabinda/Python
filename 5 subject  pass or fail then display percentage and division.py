print("Enter marks of 5 subjects")
a,b,c,d,e=int(input()),int(input()),int(input()),int(input()),int(input())
if a>=33 and b>=33 and c>=33 and d>=33 and e>=33:
    print("Result: Pass")
    per=(a+b+c+d+e)/5
    print("Percentage: ",per)
    if  per>=60:
        print("FIRST DIVISION")
    elif per>=50:
            print("SECOND DIVISION")
    else:
                print("THIRD DIVISION")
else:
    print("Result: FAIL")
