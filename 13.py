try:
    i = int(input('Введите число:\t'))
except ValueError as e:
    print('Вы ввели неправильное число')
else:
    print(f'Вы ввели {i}')
finally:
    print('Выход из программы')

def are_both_odd(A, B):
    return (A % 2 !=0) and (B % 2 != 0)
print(are_both_odd(A = 21, B = 43))


hour=int(input('Введите время'))
if 6 <= hour < 12:
    print("Утро!!!")
    month = int(input())

    if month in [3, 4, 5]:
        print("Весна")
    elif month in [6, 7, 8]:
        print("Лето")
    elif month in [9, 10, 11]:
        print("Осень")
    elif month in [12, 1, 2]:
        print("Зима")

user_database= {
    'user': 'password',
    'iseedeadpeople': 'greedisgood',
    'hesoym': 'tgm'
}
username=input('Логин')
password=input('Пароль')
def check_user(username, password):
    if username in user_database:
        if password == user_database [username]:
            return True
        else:
            return False
    else:
        return False

A = int(input('Ввидите первое число\n'))
B = int(input('Ввидите второе число\n'))
C = int(input('Ввидите третье число\n'))

if ((A < 45) and (B >=45) and (C >=45)) or \
   ((A >=45) and (B >45) and (C >=45)) or \
   ((A >=45) and (B >=45) and (C <45)):
    print('Есть число меньше 45 и только одно')
else:
    print('Числа меньше 45 нет или их несколько')


def print_ladder(n):
        for i in range(1, n + 1):
            print('*' * i)
print_ladder(n = 3)

T=[[i*j for j in range(1,11)] for i in range (1,11)]
print(T, sep="/n")

L=[int(input()) % 2 == 0 for i in range(5)]