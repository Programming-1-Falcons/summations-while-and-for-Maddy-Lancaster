num = int(input())

total = num

loops = 0

for num in range(1,num):

    loops += 1
    total += loops
print(total)
