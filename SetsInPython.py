# Sets is unique elements, immutable and unordered

s = {1, 2, 2, 3, 4, 5}

print(s)

# Empty set
empty_set = set()
print(type(empty_set))

# methods in sets

# 1. add(val)

s.add(12)
print(s) 

# 2. remove(val)

s.remove(12)
print(s)

# 3. clear(val)

s.clear()
print(s)