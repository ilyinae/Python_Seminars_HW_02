# 1. Напишите программу, которая принимает на вход
# вещественное число и показывает сумму его цифр.
# Без работы с методами строк.
# in -> out
# - 6782 -> 23
# - 0.67 -> 13
# - 198.45 -> 27

a = 123456.123456 # отладочная строка

def count_of_decimaldigits(num):                                        # число введенных знаков после запятой - совсем без строковых функций
    point_idx = str(num).find('.')                                      # не получается в общем случае из за непредсказуемой работы с типом float:    
    if point_idx != -1:                                                 # число 12345.12345 отрабатывате корректно, а 123456.123456 - уже само округляется до 123456.1234559998 и т.п.
        res = len(str(num)) - str(num).find('.')-1                      # поэтому в этой функции явно считаем сколько раз нам нужно сдвинуть запятую (на основании данных, введенных с клавиатуры)
    else:
        res = 0
    return res

def int_digit_summ(x):                                                  # суммирование цифр целого числа
    sum = 0
    while x > 0:
        sum += x % 10
        x //= 10
    return (sum)

def comma_shift(number):                                                # сдвиг запятой вправо до тех пор, пока число не станет целым
    print('Исходное: ', number)
#    while number != round(number):
#    while number % 10:
    i = 0
    iter_cou = count_of_decimaldigits(number)
    while i <= iter_cou-1:
        number *= 10
        i += 1
    print('Округлили: ', round(number))
    return (round(number))    

# while True:
#     try:
#         a = float(input('Введите вещественное число:').replace(',','.'))  # если вместо точки ввели запятую - заменим
#         break
#     except ValueError:
#         print("Видимо вы ошиблись. Нужно ввести число. Попробуйте еще раз...")

#print (f'Сумма чисел введенного числа равна {int_digit_summ(comma_shift(a))}')
int_digit_summ(comma_shift(a))