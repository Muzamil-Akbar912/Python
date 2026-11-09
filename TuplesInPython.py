# Tuples are immutable sequence of values

tup = (1, 2, 3, 4, 5)

print(tup)
print(len(tup))

# we cannot write single tuple like this
tup1 = (1) # it is treated as expression so we have to add comma in the last
print(type(tup1))

tup2 = (1,)
print(type(tup2))