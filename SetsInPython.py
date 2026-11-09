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

# 4. pop() -> remove random value

s1 = {1, 2, 2, 3, 4, 5}
s1.pop()
print(s1)

# 5. union()

s2 = {11, 12, 34}
s3 = s1.union(s2)
print(s3)

