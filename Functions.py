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