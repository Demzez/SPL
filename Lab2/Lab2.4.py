def test():
    print("Любуйтесь наздоровье:")

    try:
        number = int(input("\nВведите число: "))
        result = 100 / number
        print(f"100 / {number} = {result}")

    except ValueError:
        print("Ошибка: Это не число!")

    except ZeroDivisionError:
        print("Ошибка: Нельзя делить на ноль!")

    except Exception as e:
        print(f"Неожиданная ошибка: {e}")

    else:
        print()

    finally:
        print("Этот блок выполнится при любом раскладе.")
        print("Здесь обычно закрывают файлы, соединения и т.д.")

while True:
    test()