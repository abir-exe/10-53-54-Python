def greatest(a,b,c):
    if(a>b and a>c):
        # print("a is greatest")
        return a
    elif(b>a and b>c):
        # print("b is greatest")
        return b
    else:
        # print("c is greatest")
        return c

num1 = int(input("Enter a: "))
num2 = int(input("Enter b: "))
num3 = int(input("Enter c: "))

# greatest(num1, num2, num3)
print(greatest(num1, num2, num3))