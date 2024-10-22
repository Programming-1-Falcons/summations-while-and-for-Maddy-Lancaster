num = int(input("Enter a number: "))

total = num

loops = 0

for num in range(0,num):
    print(total)
    loops += 1
    total += loops
