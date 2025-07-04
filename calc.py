def calculator():
    print("Простой калькулятор")
    print("Выберите операцию:")
    print("1. Сложение")
    print("2. Вычитание")
    print("3. Умножение")
    print("4. Деление")

    choice = input("Введите номер операции (1/2/3/4): ")

    if choice not in ('1', '2', '3', '4'):
        print("Ошибка: неверный выбор")
        return

    try:
        num1 = float(input("Введите первое число: "))
        num2 = float(input("Введите второе число: "))
    except ValueError:
        print("Ошибка: введите корректные числа")
        return

    if choice == '1':
        result = num1 + num2
        operation = "+"
    elif choice == '2':
        result = num1 - num2
        operation = "-"
    elif choice == '3':
        result = num1 * num2
        operation = "*"
    elif choice == '4':
        if num2 == 0:
            print("Ошибка: деление на ноль")
            return
        result = num1 / num2
        operation = "/"

    print(f"\nРезультат: {num1} {operation} {num2} = {result}")

# Запуск
calculator()
