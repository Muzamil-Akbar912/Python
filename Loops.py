# loops are used repeatation of any task

# while loop
count = 1 # iterator
while(count <= 5):
    print("Hello world!", count)
    count += 1

# Break Keyword (used for terminating loop)

i = 1
while(i <= 15):
    if(i == 11):
        break
    print(i)
    i += 1

print("Outside loop now.......")

# Continue Keyword (used for skiping the current iteration)

j = 1

while(j <= 10):
    if(j % 3 == 0):
        j += 1
        continue
    print(j)
    j +=1

print("Outside loop now.......")

# for loop (used for sequential traversal)

str = "hello"

# in => Membership operator(used for checking presence of value)
for var in str:
    print(var)

if('x' in str):
    print("x exists in str")
else:
    print("x does exists in str")

# range(start, stop, step) -> it generates sequences

for k in range(5):
    print(k)

print("Outside loop now.......")

for k in range(1, 10):
    print(k)

print("Outside loop now.......")

for k in range(1, 10, 2):
    print(k)

print("Outside loop now.......")