upperPairs = 0
lowerPairs = 0

word = input("Enter a word: ")
for i in range(len(word)-1):
    letter1 = word[i]
    letter2 = word[i+1]

    if letter1.isupper() and letter2.isupper():
        upperPairs += 1
    elif letter1.islower() and letter2.islower():
        lowerPairs += 1
    else:
        continue

print(f"Count of letters: {len(word)}")
print(f"Upper Pairs: {upperPairs}")
print(f"Lower Pairs: {lowerPairs}")
