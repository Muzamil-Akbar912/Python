# In python, Strings are immutable(does not change)

word1 = "I love"
word2 = "Python"

# length of string
print(len(word1))

# concatenate
print(word1 + " " + word2)

# indexing

for ch in word2:
    print(ch)


# Slicing using positive index

str = "I study from ApnaCollege"

print(str[0:7]) # last index is not included
print(str[0:]) # include all values
print(str[:])
print(str[0:len(str)])

# Slicing using negative index

print(str[-4:-2])

# String formating (used for dynamic strings), methods we use :
# 1. format()  -> python 3
# 2. f-strings 

# Normal formatting
a = 5
b = 10
sum = a + b

print("Language is {}".format("Python"))
print("Sum of {} and {} is {}".format(a, b, sum))

# index based formatting
print("Sum of {0} and {1} is {2}".format(a, b, sum))
print("Sum of {1} and {0} is {2}".format(a, b, sum))

# value based formatting
print("Values of variables is {x} and {y}".format(x = 11, y = 10))

# f-strings -> version 3.6 (we use literal string interpolation)
n = 11
m = 10

print(f"Sum of {n} and {m} is {n + m}")
print(f"Average of {n} and {m} is {(n + m) / 2}")
