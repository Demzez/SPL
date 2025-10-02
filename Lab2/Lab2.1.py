wordList = input("Enter a string: ").split()
print(f"Количество слов: {len(wordList)}")
print(f"Самое длинное слово: {max(wordList, key=len)}")

list = [range(10)]
for item in list:
    print(item)


print(type(list))
