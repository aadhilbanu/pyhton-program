arr = [10, 20, 30, 40, 50]
key = int(input("Enter element to search: "))

found = False
for i in arr:
    if i == key:
        found = True
        break

if found:
    print("Element found")
else:
    print("Element not found")
