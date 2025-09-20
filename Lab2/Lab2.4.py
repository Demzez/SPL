def test():
    print("Простая демонстрация:")

    try:
        number = int(input("Введите число: "))
        result = 100 / number
        print(f"100 / {number} = {result}")

    except ValueError:
        print("Ошибка: Это не число!")

    except ZeroDivisionError:
        print("Ошибка: Нельзя делить на ноль!")

    except Exception as e:
        print(f"Неожиданная ошибка: {e}")

    finally:
        print("Этот блок выполнится ВСЕГДА!")
        print("Здесь обычно закрывают файлы, соединения и т.д.")


test()