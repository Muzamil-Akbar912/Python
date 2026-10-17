# if statement
age = 21

if age >= 18:
    print("you can vote")
    print("you can drive")

# if else statement

if age >= 18:
    print("you can vote")
else:
    print("you can't vote")

# elif statement
color = input("Enter color: ")

if color == "red":
    print("stop")
elif color == "green":
    print("go")
elif color == "yellow":
    print("look")
else:
    print("Wrong color for traffic lights")

# Nesting
username = input("Enter username : ")
password = input("Enter password : ")

if(username == "admin" and password == "pass"):
    print("success")
else:
    if(username != "admin"):
        print("wrong username")
    else:
        print("wrong password")