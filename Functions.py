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