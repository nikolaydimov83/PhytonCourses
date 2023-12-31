def factorial(num1):
    if num1==1:
        return 1
    return num1*factorial(num1-1)

num1=int(input())
num2=int(input())

print(f"{factorial(num1)/factorial(num2):.2f}")
    