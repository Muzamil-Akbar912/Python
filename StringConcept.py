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


# Slicing

str = "I study from ApnaCollege"

print(str[0:7]) # last index is not included
print(str[0:]) # include all values
print(str[:])
print(str[0:len(str)])