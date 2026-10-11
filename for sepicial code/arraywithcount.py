arr = []
for i in range(7):
    num = input("enter number:-")
    arr.append(num)

print(arr)
result = {}
for num in arr:
    if num in result:
        result[num] += 1
    else:
        result[num] = 1
print(result)
