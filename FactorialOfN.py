def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact = fact * i
    return fact

num = int(input("Enter the value of num : "))
res = factorial(num)
print("Factorial of number",num,"=",res)
