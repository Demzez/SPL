tupleList = (1, 2, 3, 4, 5)
minEvenElement = tupleList[0]
isOk = True

for element in tupleList:
    if element % 2 == 0 and isOk == True:
        minEvenElement = element
        isOk = False
    if element < minEvenElement and element % 2 == 0:
        minEvenElement = element

print(f"Минимальный четный элемент картежа: {minEvenElement}")