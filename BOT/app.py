#import redis

#red = redis.Redis(
#    password='zbJZvAdN56Tdz3WfZpQCmt3RyhEo0bWX',
#    host='redis-16762.c84.us-east-1-2.ec2.cloud.redislabs.com',
#    port=16762
#)

#red.set('var1' , 'value1')  # записываем в кеш строку "value1"
#print(red.get('var1'))   # считываем из кэша данных
#Но на этом ещё не всё. Вся загвоздка здесь в том, что данные, нами записанные, не зависят от текущей сессии. Они не стираются после того, как скрипт закончит работу. Их состояние зависит только от самого хранилища, которое крутится у нас в облаке.
#Давайте теперь удалим некоторые строчки и убедимся, что данные, которые мы записывали в предыдущей сессии, сохранились.

#import redis

#red = redis.Redis(
#    password='zbJZvAdN56Tdz3WfZpQCmt3RyhEo0bWX',
#    host='redis-16762.c84.us-east-1-2.ec2.cloud.redislabs.com',
#    port=16762
#)

#print(red.get('var1'))   # считываем из кэша данных

#Давайте теперь попробуем записать в кэш что-нибудь посложнее, например, словарь.

#import redis
#import json  # так-так-так, кто это тут у нас? Наш старый друг Джейсон заглянул на огонёк! Ну привет, чем ты сегодня нас порадуешь?

#red = redis.Redis(
#    host='redis-16762.c84.us-east-1-2.ec2.cloud.redislabs.com',
#    port=16762,
#    password='zbJZvAdN56Tdz3WfZpQCmt3RyhEo0bWX'
#)

#dict1 = {'key1': 'value1', 'key2': 'value2'}  # создаём словарь для записи
#red.set('dict1', json.dumps(dict1))  # с помощью функции dumps() из модуля json превратим наш словарь в строчку
#converted_dict = json.loads(
#    red.get('dict1'))  # с помощью знакомой нам функции превращаем данные полученные из кэша обратно в словарь
#print(type(converted_dict))  # убеждаемся, что получили действительно словарь
#print(converted_dict)  # ну и выводим его содержание


#Давайте теперь попробуем записать в кэш что-нибудь посложнее, например, словарь.

#import redis
#import \json  # так-так-так, кто это тут у нас? Наш старый друг Джейсон заглянул на огонёк! Ну привет, чем ты сегодня нас порадуешь?

#red = redis.Redis(
#   password='zbJZvAdN56Tdz3WfZpQCmt3RyhEo0bWX',
#   host='redis-16762.c84.us-east-1-2.ec2.cloud.redislabs.com',
#   port=16762
#)

#dict1 = {'key1': 'value1', 'key2': 'value2'}  # создаём словарь для записи
#red.set('dict1', json.dumps(dict1))  # с помощью функции dumps() из модуля json превратим наш словарь в строчку
#print(type(converted_dict))  # убеждаемся, что получили действительно словарь
#print(converted_dict)  # ну и выводим его содержание

#давайте научимся удалять данные из кэша по ключу

#import redis
#import json

#red = redis.Redis(
#    password='zbJZvAdN56Tdz3WfZpQCmt3RyhEo0bWX',
#    host='redis-16762.c84.us-east-1-2.ec2.cloud.redislabs.com',
#    port=16762
#)

#red.delete('dict1')  # удаляются ключи с помощью метода .delete()
#print(red.get('dict1'))

#Напишите программу, которая будет записывать и кэшировать номера ваших друзей. Программа должна уметь воспринимать несколько команд:
# записать номер,
# показать номер друга в консоли при вводе имени или же удалить номер друга по имени.
# Кэширование надо производить с помощью Redis.
# Ввод и вывод информации должен быть реализован через консоль (с помощью функций input() и print()).

red = redis.Redis(
    password='zbJZvAdN56Tdz3WfZpQCmt3RyhEo0bWX',
    host='redis-16762.c84.us-east-1-2.ec2.cloud.redislabs.com',
    port=16762
)

cont = True

while cont:
    action = input('action:\t')
    if action == 'write':
        name = input('name:\t')
        phone = input('phone:\t')
        red.set(name, phone)
    elif action == 'read':
        name = input('name:\t')
        phone = red.get(name)
        if phone:
            print(f'{name}\'s phone is {str(phone)}')
    elif action == 'delete':
        name = input('name:\t')
        phone = red.delete(name)
        if phone:
            print(f"{name}'s phone is deleted")
        else:
            print(f"Not found {name}")
    elif action == 'stop':
        break