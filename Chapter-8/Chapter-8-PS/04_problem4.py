def sum(n):
    if(n==1):
        return 1
    elif(n<1):
        return "This is not a natural number"
    return sum(n-1) + n

num = int(input("Enter your number: "))

print(sum(num))