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

# some functions in lists

# 1. append(value) function -> add value in last of list

num = [1, 3, 5, 7, 9]
num.append(11)
print(num)

# 2. insert(index, value) function -> insert value in any index

num.insert(3, 17)
print(num)

# 3. sort() function -> sort the list in ascending or descending order

num.sort() # ascending order
print(num)

num.sort(reverse=True) # descending order
print(num)

# 4. reverse() function -> reverse the list

lst = [1, 2, 3, 4, 5, 6, 11, 34, 21, 12]
lst.reverse()
print(lst)