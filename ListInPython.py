# Lists is mutable sequence of values

marks = [99, 89, 100, 63, 92]

print(marks)
print(len(marks))

# change the value in any index
marks[2] = 123
print(marks)

# make sublists using slicing

print(marks[1:3])
print(marks[3:len(marks)])