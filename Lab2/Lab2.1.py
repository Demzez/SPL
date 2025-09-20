str = input("Enter a string: ")
wordList = str.split();
print(f"Количество слов: {len(wordList)}")
print(f"Самое длинное слово: {max(wordList, key=len)}")

