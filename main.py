# This is a sample Python script.
import math
from typing import Dict


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
# name= 'Ivan"

a = 5 + 5
print(a)
a = 5/2
b = 5//2
print(a)
print(b)
#
a = round(10/3.0, 2)
print(a)
# функция преобразования - int() целочисленное преобразование

print(math.pow(2, 6))
print(math.sqrt(9))
print(math.pi)

print(bin(8))
# String

name = 'Иван Иванович'
# по индексу
# print(name[-1])
# срез строки [start:stop:step]

# print(name[1:6:2])
# concat (Конкатинация- суммирование строк)
name='Иван  '
fullname= 'Иванов'
res = name + fullname
print(res)

#Methods string
#string= 'Hello'
#res = string.lower()
#print(res)

#string= 'Hello'
#res = string.upper()
#print(res)

#name = input('Введите Ваше имя ' )
#name_start = name[0].upper()
#name_end = name[1:].lower()
#res = name_start + name_end
#print(res)

#Цикл
# for ... in(по буквам в столбец)
#for i in name:
#    print(i)
#exam = 'Привет мир'
#count = 0
#for i in exam: # и
#   if i == 'и':
#        count= count + 1 #
#print(count,'буквы "и" в данной строке')

#проверка на вхождения
#in и  not in
#a = 'hello'
#b = 'hello world'
#print(a in b)

# len() возвращает длину строки
# string = 'hello'
# print(len(string))


# split () -разбивает строки по разделителю ;
# join() -собирает строку из списка ;
# replace()- заменяет к-л шаблон в строке
# \n- перевод на следующую строку
print('hello\nworld')

#format
# порядок с позиционными аргументами -{}
string = "{1}, {0}, {2}".format('Петя','Ваня','Катя')
print(string)
# порядок по ключевым словам
string = "{s}, {b}, {j}".format( j='Петя', s='Ваня', b='Катя')
print(string)

# f-строки
a= 'Ivan'
res= f'{a}, hello'
print(res)

#list -список []
numbers= [1,2,3,4,5,'hello', True]
print(numbers)
print(numbers[5] * 6)
#можно через функцию list()
#numbers_1=list()
#print(numbers_1)
print(numbers[-1])

# Перебор списка делается через цикл for in
people=['Ivan','Tom', 'Kate']
for person in people:
    print(person)
#получаются элементы из списка

#Методы списка (Methods list)
# append (item)- опред.элемент в конц списка
people=['Ivan','Tom', 'Kate']
new_person =people.append('Bob')
print(people)
#insert(item)-добавляет элемент в список по индексу
people=['Ivan','Tom', 'Kate']
new_person =people.append('Bob')
print(people.insert(1, 'Bill'))
print(people)
#remove(item)-удаляет элемент, только первое вхождение. Повторяющейся не удалится.
print(people.remove('Bill'))
print(people)
#in
people=['Ivan','Tom', 'Kate']
if 'Tom' in people :
    people.remove('Tom')
    print(people)

#count()-узнать количество элиментов
people=['Ivan','Tom', 'Kate', 'Tom']
people_count=people.count('Tom')
print(people_count)

#sort
people=['Ivan','Tom', 'Kate', 'Tom']
a=[4,3,2,1]
print(sorted (a))
print(people_count)

#[-1,-3,0,1,2,3]
# revers
#копирование часть списка через старт и степ(start and step)

#список в списке
people= [
    ['Ivan', 29],
    ['Kate', 27],
    ['Bob', 32]
]
print(people[0][1])

#Перебор (вложенный цикл)
for person in people:
    print(person)

for person in people:
    for item in person:
        print(item)

 # Tuple (Кортеж )     используются ()
 # Словари {keys: values}

 #users = {1: 'Tom', 2: 'Bob', 3: 'Kate'}
 #users[1]= 'Tom2'
 #print(users)
# users= {1:'Tom', 2:'Bob', 3:'Kate'}
 #key =2
#if key in users:
#     user = users[key]
#     print(user)
#else:
#   print('элемент не найден')


#множества set()
users = {'Tom','Bob','Kate'}
users.add('Sam')
print(users)


# union() Объединяет два множества и возвращает новое множество
users_1 = {'Tom','Bob','Kate'}
users_2 = {'Sam','Kate','Bob'}
users_3 = users_1.union(users_2)
print(users_3)
#intersection -опреции пересечения множества и возвращает новое множество
users_1 = {'Tom','Bob','Kate'}
users_2 = {'Sam','Kate','Bob'}
users_3 = users_1.union(users_2)
users_4 = users_1.intersection(users_2)
users_5 = users_1.difference(users_2)
users_6 = users_1.symmetric_difference(users_2)
print(users_6)






