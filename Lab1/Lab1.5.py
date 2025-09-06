products = {
    "Масло моторное": ["Синтетическое масло 5W-30", 2500, 15],
    "Воздушный фильтр": ["Бумажный фильтр", 1200, 8],
    "Тормозные колодки": ["Керамические колодки", 4500, 5],
    "Аккумулятор": ["Свинцово-кислотный 60Ah", 8000, 3],
    "Свечи зажигания": ["Иридиевые свечи", 2000, 20]
}

def view_descriptions():
    print("\n--- ОПИСАНИЯ ТОВАРОВ ---")
    for product, info in products.items():
        print(f"{product} - {info[0]}")


def view_prices():
    print("\n--- ЦЕНЫ ТОВАРОВ ---")
    for product, info in products.items():
        print(f"{product} - {info[1]} руб.")


def view_quantities():
    print("\n--- КОЛИЧЕСТВО ТОВАРОВ ---")
    for product, info in products.items():
        print(f"{product} - {info[2]} шт.")


def view_all_info():
    print("\n--- ВСЯ ИНФОРМАЦИЯ ---")
    for product, info in products.items():
        print(f"{product}: {info[0]}, Цена: {info[1]} руб., Количество: {info[2]} шт.")


def make_purchase():
    print("\n--- ПОКУПКА ---")
    print("Введите название товара и количество через пробел")

    total_price = 0
    receipt = []

    while True:
        # Проверки
        user_input = input("Товар и количество (или 'n' для выхода): ").strip()
        if user_input.lower() == 'n':
            break

        parts = user_input.split()
        if len(parts) < 2:
            print("Ошибка: введите название и количество через пробел")
            continue

        product_name = ' '.join(parts[:-1]) # объединение нескольких элементов кроме последнего в одну строку
        if parts[-1].isdigit():
            count = int(parts[-1])
        else:
            print("Ошибка: количество должно быть числом")
            continue

        if product_name not in products:
            print(f"Ошибка: товар '{product_name}' не найден")
            continue

        product_info = products[product_name]
        if count > product_info[2]:
            print(f"Ошибка: недостаточно товара. В наличии: {product_info[2]} шт.")
            continue

        if count <= 0:
            print("Ошибка: количество должно быть положительным")
            continue

        # Покупка
        price = product_info[1] * count
        total_price += price
        product_info[2] -= count

        # Добавляем в чек
        receipt.append((product_name, count, price))
        print(f"Добавлено: {product_name} x{count} = {price} руб.")

    # Печатаем чек
    if receipt:
        print("\n=== ВАШ ЧЕК ===")
        print("Товар\t\tКоличество\tСтоимость")
        print("-" * 40)
        for item in receipt:
            print(f"{item[0]}\t{item[1]} шт.\t\t{item[2]} руб.")
        print("-" * 40)
        print(f"ИТОГО: {total_price} руб.")
        print("Спасибо за покупку!")
    else:
        print("Покупка отменена")


while True:
    print("\n=== МАГАЗИН АВТОЗАПЧАСТЕЙ ===")
    print("1. Просмотр описания")
    print("2. Просмотр цены")
    print("3. Просмотр количества")
    print("4. Вся информация")
    print("5. Покупка")
    print("6. До свидания")

    choice = input("Выберите пункт меню (1-6): ")

    if choice == "1":
        view_descriptions()
    elif choice == "2":
        view_prices()
    elif choice == "3":
        view_quantities()
    elif choice == "4":
        view_all_info()
    elif choice == "5":
        make_purchase()
    elif choice == "6":
        print("До свидания! Приходите еще!")
        break
    else:
        print("Неверный выбор. Попробуйте снова.")

