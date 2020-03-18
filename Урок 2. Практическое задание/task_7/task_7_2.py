"""
7.	Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
 где n - любое натуральное число.

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ РЕКУРСИЮ
"""


"""
Данное равенство доказывается через
математическую индукцию 

1) n = 1 => 1 = 1 * 2 / 2
2) Пусть верно для n
3) Докажем равенство для n+1

1 + 2 + .... + n + (n+1) = (n+1)(n+2)/2 

n(n+1)/2 + (n+1) = (n+1) [ n/2 + 1 ] = (n+1)(n+2)/2
ч.т.д
4)По принципу мат индукции данное равенство справедливо для 
любых натуральных чисел 
"""


def left_part(n):

    result = 1
    for i in range(2, n+1):
        result += i
    return result


def right_part(n):
    return n*(n+1)/2


def recursive_check(n):

    if n == 0:
        return True
    elif left_part(n) != right_part(n):
        return False
    else:
        return recursive_check(n-1)


N = int(input("Введите натуральное число, до которого выполнять проверку\n"))
CHECK = recursive_check(N)

if CHECK:
    print(f"Данное равенство справедливо для всех\nнатуральных чисел вплоть до числа {N}")
else:
    print(f"Данное равенство не спаведливо для всех натуральных чисел")
