# functions are block of statement that perform specific task(or functions are reuseable component of code).

def hello():
    print("Hello");

for i in range(5):
    hello()

# function definition
def sum(a, b): # parameters
    s = a+b
    return s

# function call
ans = sum(3, 7) # arguments
print(ans)

# calculate average
def cal_avg(a, b, c):
    sum = a + b + c
    average = sum / 3
    return average

result = cal_avg(10, 20, 30)
print(result)

# default parameters (yeh last parameter mai assign ki jaati hai na ki first parameter mai)

def addition(a, b = 1):
    res = a + b
    return res

ans1 = addition(7)
print(ans1)

# Lambda function (we can only have single expression, used in higher order functions)

sum2 = lambda a,b: a+b

print(sum2(4, 5))

avg = lambda a, b, c : (a+b+c)/3

print(avg(10, 20, 30))