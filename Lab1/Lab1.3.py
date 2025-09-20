list1 = [1, -2, 3, 0, 4, -4, -1, 3, -2, 4, 0, -3, 2, 6]
sumPositiveElements = 0
sumZeroElements = 0
isOk = False
zeroCount = 0

for element in list1:
    if element > 0:
        sumPositiveElements += element
    if element == 0:
        zeroCount += 1
        if zeroCount <= 2:
            isOk = not isOk
            continue
    if isOk:
        sumZeroElements += element

print(f"Positive: {sumPositiveElements}")
if zeroCount <= 1:
    print(f"No elements between zero numbers. {0}")
else:
    print(f"Zero: {sumZeroElements}")
