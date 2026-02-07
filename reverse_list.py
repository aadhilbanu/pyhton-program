arr = [10, 20, 30, 40]
rev = []

for i in range(len(arr) - 1, -1, -1):
    rev.append(arr[i])

print("Reversed list:", rev)
