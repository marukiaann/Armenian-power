import math

def exp_series(x, terms=20):
    r"""
    Вычисление экспоненты через сумму ряда.
    e^x = \sum_{n=0}^{\infty} (x^n / n!)
    """
    result = 0
    for n in range(terms):
        result += (x ** n) / math.factorial(n)
    return result

def sin_series(x, terms=20):
    r"""
    Вычисление синуса через сумму ряда.
    sin(x) = \sum_{n=0}^{\infty} (-1)^n * x^(2n+1) / (2n+1)!
    """
    result = 0
    for n in range(terms):
        sign = (-1) ** n
        result += sign * (x ** (2 * n + 1)) / math.factorial(2 * n + 1)
    return result

def cos_series(x, terms=20):
    r"""
    Вычисление косинуса через сумму ряда.
    cos(x) = \sum_{n=0}^{\infty} (-1)^n * x^(2n) / (2n)!
    """
    result = 0
    for n in range(terms):
        sign = (-1) ** n
        result += sign * (x ** (2 * n)) / math.factorial(2 * n)
    return result

def calculate_formula1(x, terms=20):
    r"""
    Вычисление синуса через сумму ряда.
    sin(x) = \sum_{n=0}^{\infty} (-1)^n * x^(2n+1) / (2n+1)!
    """
    return sin_series(x, terms)

def calculate_formula2(x, terms=20):
    r"""
    Вычисление косинуса через сумму ряда.
    cos(x) = \sum_{n=0}^{\infty} (-1)^n * x^(2n) / (2n)!
    """
    return cos_series(x, terms)


def main_menu():
    """
    Главное меню программы.
    """
    while True:
        print("\nМеню:")
        print("1. Вычислить формулу 1")
        print("2. Вычислить формулу 2")
        print("3. Выход")

        choice = input("Выберите действие: ")
        if choice == "1":
            try:
                x = float(input("Введите значение x: "))
                print(f"Результат: {calculate_formula1(x)}")
            except ValueError as e:
                print(f"Ошибка: {e}")
        elif choice == "2":
            try:
                x = float(input("Введите значение x: "))
                print(f"Результат: {calculate_formula2(x)}")
            except ValueError as e:
                print(f"Ошибка: {e}")
        elif choice == "3":
            print("Выход из программы.")
            break
        else:
            print("Некорректный ввод. Попробуйте снова.")

if __name__ == "__main__":
    main_menu()
