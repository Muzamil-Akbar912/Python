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

a = 5
b = 10
sum = a + b

print("Language is {}".format("Python"))
print("Sum of {} amd {} is {}".format(a, b, sum))