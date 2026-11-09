# Tuples are immutable sequence of values

tup = (1, 2, 3, 4, 5)

print(tup)
print(len(tup))

# we cannot write single tuple like this
tup1 = (1) # it is treated as expression so we have to add comma in the last
print(type(tup1))

tup2 = (1,)
print(type(tup2))

# slicing in tuples
print(tup[1:3])
print(tup[1:len(tup)])

# some methods used in tuples

# 1. index(val) -> returns first occurance idx

t = (1, 2, 2, 2, 3, 4, 5, 6,)
print(t.index(2))

# 2. count(val) -> prints count of any value
print(t.count(2))