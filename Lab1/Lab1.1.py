even = 0
odd = 0

number = int(input("Enter a number: "))
number = abs(number)

if number == 0:
    even = 1
else:
    while number > 0:
        digit = number % 10
        if digit % 2 == 0:
            even += 1
        else:
            odd += 1
        number //= 10

print("Even:", even)
print("Odd:", odd)