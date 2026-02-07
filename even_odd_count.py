arr = [10, 15, 20, 25, 30]
even = 0
odd = 0

for i in arr:
    if i % 2 == 0:
        even += 1
    else:
        odd += 1

print("Even count:", even)
print("Odd count:", odd)
