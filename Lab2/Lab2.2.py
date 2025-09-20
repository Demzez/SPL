def process_data(data):
    if isinstance(data, dict):
        # Сортировка словаря
        asc = dict(sorted(data.items()))
        desc = dict(sorted(data.items(), reverse=True))
        return {"ascending": asc, "descending": desc}

    elif isinstance(data, list):
        # Подсчет букв и чисел в списке
        letters = sum(1 for item in data if isinstance(item, str) and item.isalpha())
        numbers = sum(1 for item in data if isinstance(item, (int, float)))
        return {"letters": letters, "numbers": numbers}

    elif isinstance(data, int):
        # Проверка на простое число
        if data < 2:
            return False
        for i in range(2, int(data ** 0.5) + 1):
            if data % i == 0:
                return False
        return True

    elif isinstance(data, str):
        # Поиск слов-палиндромов
        words = data.split()
        palindromes = [word for word in words if word.lower() == word.lower()[::-1]]
        return palindromes

    else:
        return "Неподдерживаемый тип данных"


# Тестирование всех случаев
print("\nTest1 - словарь:")
dictX = {"a": 1, "c": 2, "b": 3}
print(process_data(dictX))

print("\nTest2 - список:")
listX = ["a", "b", 1, 2, "c", 5, 6, 7, 8, 9]
print(process_data(listX))

print("\nTest3 - простое число:")
numX = 23
print(process_data(numX))

print("\nTest4 - составное число:")
numY = 15
print(process_data(numY))

print("\nTest5 - строка:")
strX = "I am a string its no palindrom, level"
print(process_data(strX))