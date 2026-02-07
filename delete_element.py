arr = [10, 20, 30, 40, 50]
value = int(input("Enter value to delete: "))

if value in arr:
    arr.remove(value)
    print("Updated list:", arr)
else:
    print("Element not found")
