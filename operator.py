#Сложение
a = 3
b = 2
a = a + b
print(a)  #Присвоили результат уже имеющейся переменной

#Вычитание
a = 10
b = 5
a -= b
print(a)

#Умножение
a = 0.5 
b = 10
a *= b
print(a)

#Деление
a = 40
b = 8
a /= b
print(a)

#Получение целой части от деления
a = 45
b = 8
a //= b
print(a)

#Получение остатка от деления
a = 19
b = 7
a %= b
print(a)

#Возведение в степень
a = 25
b = 0.5
a **= b
print(a)

#Работа с комплексными числами

a = complex(3, 2)
print(a)

a = complex(5, -5)
print(a.real) #Получаем действительную часть
print(a.imag) #Получаем мнимую часть

#Сопряжение комплексного числа
a = (3 + 2j)
print(a.conjugate()) #Получение конъюгата

#Арифметические операции действительных чисел
a = 1 + 2j
b = 4 + 3j
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a ** b)
# print(a % b)  Нельзя выполнить
# print(a // b) Нельзя выполнить

#Фаза
import cmath
import math

a = 7 + 7j
b = cmath.phase(a)
print('Cmath Module:', b)

b = math.atan(a.imag/a.real)
print('Math Module:', b)

