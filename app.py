print("Calculator")
print("Enter first number")
a=int(input())
print("Enter second number")
b=int(input())
print("Enter Operation to be done")
c=input().strip()
if c=="add":
    print(a+b)
elif c=="sub":
    print(a-b)
elif c=="mul":
    print(a*b)
elif c=="div":
    print(a/b)
else:
    print("Invalid Operation")
print("Exiting Calculator")
