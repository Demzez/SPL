firstWord = input("Enter first word: ").lower()
secondWord = input("Enter second word: ").lower()

charsWord1 = list(firstWord)
charsWord2 = list(secondWord)

n1 = len(charsWord1)
n2 = len(charsWord2)


for i in range(max(n1, n2)):

    if i < n1:
        for j in range(0, n1 - i - 1):
            if charsWord1[j] > charsWord1[j + 1]:
                charsWord1[j], charsWord1[j + 1] = charsWord1[j + 1], charsWord1[j]

    if i < n2:
        for j in range(0, n2 - i - 1):
            if charsWord2[j] > charsWord2[j + 1]:
                charsWord2[j], charsWord2[j + 1] = charsWord2[j + 1], charsWord2[j]


if charsWord1 == charsWord2:
    print("Anagrams!")
else:
    print("Not anagrams!")