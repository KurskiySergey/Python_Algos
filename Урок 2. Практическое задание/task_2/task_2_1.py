"""
2.	Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, то у него 3 четные цифры
(4, 6 и 0) и 2 нечетные (3 и 5).

Подсказка:
Для извлечения цифр числа используйте арифм. операции

Пример:
Введите натуральное число: 44
В числе 44 всего 2 цифр, из которых 2 чётных и 0 нечётных

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ ЦИКЛ
"""


EVEN_COUNT = 0
ODD_COUNT = 0

try:
    VALUE = int(input("Введите натуральное число\n"))
    if VALUE < 0:
        print("Натуральное число больше нуля")
    else:
        while VALUE > 0:

            TMP = VALUE % 10
            VALUE = VALUE // 10
            if TMP % 2 == 0:
                EVEN_COUNT += 1
            else:
                ODD_COUNT += 1

        print(
            f"В данном числе {EVEN_COUNT} четных и {ODD_COUNT} нечетных цифр")

except ValueError:
    print("Нужно ввести число")
