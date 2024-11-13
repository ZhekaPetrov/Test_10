a = 'Привет!'  #Цикл while
b = 1
while b < 3:
    print(a)
    b += 1
print()

#Цикл for
a = [1, 2, 3] #Выводим каждый эелемент по отдельности
for i in a:
    print(b)
print()

for i in range(1, 4):  #range() - диапазон
    print(i)
print()

for i in range(3, 12, 3): #Третее число означает шаг, с которым числа следуют друг за другом
    print(i)
print()

a = [i for i in range(1, 4)]  #Быстрая генерация списков
print(a)
print()

print([i for i in range(1, 10) if i % 2 == 0]) #Сразу печатаем список где выводятся только четные числа
print()

print([i ** 2 for i in range(1, 10) if i % 2 == 0]) #Выводим квадраты четных чисел
print()

#Прерывание цикла ключевым словом Break
a = 'Hello, Anya'  #Если встречается запятая, цикл дострочно завершается
for i in a:
    if i == ',':
        break
    print(i)
print()

for i in range(1, 7):    #Пропускаем числа с помощью continue
    if i == 5 or i == 3 or i == 6:
        continue
    print(i)
print()

#else как последнее дейсвтие в цикле
a = 'I love you, Anya'  #Если в предложении нету запятых, то выполняется функция else
for i in a:
    if i == ',':
        break
    print(i)
else:
    print('Данное признание не содержит запятых')
print()

while 'yes' == 'no':   #esle работает даже если цикл не совершил ни одного витка
    print('Чтооо, оно работает?))')
else:
    print('Как ожидаемо')
print()

#Бесконечный цикл
#while True: #Пока истинно
#    pass #pass - оператор-заглушка, который ничего не делает

while 1: #Пока проверяемое значение - цикл никогда не начнется
    pass

while 0 #- цикл никогда не начнется

while 1 == 1:  #Если поставить пустой элемент, то цикл не начнется
    pass
while 0 != 1:
    pass

