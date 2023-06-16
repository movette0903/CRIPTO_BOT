#Синтаксис функции
#def имя функции(Что делает?) (аргументы):
#   инструкции
#   return -список выражений(
#имя функции()
#возвращаемое значение return

#def greet(name):
#    print('Привет ' + name + '. Доброе утро!')
#greet('Джон')


#def absolute_value(num):
#    if num >=0:
#        return num
#    else:
#        return -num
#print(absolute_value(2))
#print(absolute_value(-4))

#область видимости (scope) и время жизни переменной

#def my_func():
#    x = 18
#    print('значение внутри функции', x)
#x = 28
#my_func()
#print('значение вне функции', x)

# аргументы функции
#фиксированное количество аргументов

def greet(name, age='28'):
     print('Привет ' + name + '. Доброе утро!' + 'мне '+ age +' лет')
greet('Джон')

# именновый аргумент

#def greet(name= 'Джон', age='28'):
#    print('Привет ' + name + '. Доброе утро!' + 'Мне ' + age + ' лет')
#greet()
#greet(name='Ivan', age='35')

#произвольный список аргументов
#*

#def greet(*names):
#    for name in names:
#        print('Hello', name)
#greet('Kate', 'John', 'Boris')

#def adder(*nums):
#    sum=0
#    for n in nums:
#        sum += n
#    print('sum=', sum)
#adder(3,5,6,7,8)

x='глобальная переменная'
def foo():
    print('x внутри функции', x)
foo()
print('x вне функции', x)

#x='глобальная переменная'
#def foo():
#    x = x * 2
#    print(x)
#foo()

#локальные переменные

#def foo():
#   y='локальная перменная'
#    print(y)
#foo()

#x = 'global veriable'
#def foo():
#    global x
#   y = 'local variable'
#    x = x * 2
#   print(x)
#    print(y)
#foo()

#x = 5
#def foo():
#   x = 10
#    print('local variable x =', x)
#foo()
#print('global variable x=', x)

# не локальные перменные используются во вложенные функции
# nonlocal
#def outer():
#    x = 'local variable'
#    def inner():
#        nonlocal x
#        x = 'nonlocal variable'
#        print('вложенная функция', x)
#   inner()
#    print(':', x)
#outer()

# Замыкание

def say():
    greeting = ' Hello'
    def display():
        print(greeting)
    display()
say()

#вернуть функцию из функции
def say():
    greeting = 'Hello'
    def display():
        print(greeting)
    return display()
print(say())

def say():
    greeting = 'Hello'
    print(hex(id(greeting)))
    def display():
        print(hex(id(greeting)))
        print(greeting)
    return display
fn = say()
fn()
#print(fn. __closure__)
# 1. функция say()
# 2. замыкание

# Декораторы
def net_price(price, tax):
    return price * (1 + tax)

def currency(fn):
    def wrapper(*args, **kwargs):
        result = fn(*args,  **kwargs)
        return f'${result}'
    return wrapper
net_price = currency(net_price)
print(net_price(100, 0.05))

#декаратор синтаксис
# функция = декаратор(функция)

#

def currency(fn):
    def wrapper(*args, **kwargs):
        result = fn(*args,  **kwargs)
        return f'${result}'
    return wrapper
@currency
def net_price(price, tax):
    return price * (1 + tax)
net_price = currency(net_price)
print(net_price(100, 0.05))

# lambda аргументы: выражения
double = lambda x: x * 2
print(double(5))

# map
my_list = [2,5,56,7,8,9,6]
new_list = list(map(lambda  x: x * 2, my_list))
print(new_list)








