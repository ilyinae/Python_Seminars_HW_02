# 2. Напишите программу, которая принимает на вход число N
# и выдает набор произведений чисел от 1 до N в виде списка.
# 1 - 1 * 1, 2 - 1 * 2, 3 - 1 * 2 * 3, 4 - 1 * 2 * 3 * 4 и т.д.
# - 4 -> [1, 2, 6, 24]
# - 6 -> [1, 2, 6, 24, 120, 720]

#n = 6 # отладочная строка
def fact(x): #рекурсивное вычисление факториала
    if x == 1 or x == 0:
        return 1
    else:
        return x*fact(x-1)    

while True:
    try:
        n = int(input('Введите целое число: '))
        break
    except ValueError:
        print("Видимо вы ошиблись. Нужно ввести целое число. Попробуйте еще раз...")

outlist = []
for i in range(1, n+1):
    outlist.append(fact(i))

print(outlist)