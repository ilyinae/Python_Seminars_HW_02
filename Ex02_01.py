# 1. Напишите программу, которая принимает на вход
# вещественное число и показывает сумму его цифр.
# Без работы с методами строк.
# in -> out
# - 6782 -> 23
# - 0.67 -> 13
# - 198.45 -> 27

#a = 12345.12345
a = 198.45

def int_digit_summ(x): # суммирование цифр целого числа
    sum = 0
    while x > 0:
        sum += x % 10
        x //= 10
    return (sum)

def comma_shift(number): # сдвиг запятой вправо до тех пор, пока число не станет целым
    while number != round(number):
        number *= 10
    return (int(number))    

print (int_digit_summ(comma_shift(a)))