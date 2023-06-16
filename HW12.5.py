pi = 31.4159265
print ("%.4e" % (pi))

#HW 12.5.5

# string=input("Ввидите числа через пробел")
# list_of_strings = string.split()
# list_of_numbers = list(map(int, list_of_strings))
# print(sum(list_of_numbers[::3]))

# L=list(map(float, input().split()))
# L[0], L[-1] = L[-1], L[0]
# L.append(sum(L))
# print

# string=input("Ввидите числа через пробел")
# list_of_strings = string.split()
# list_of_numbers = list(map(int, list_of_strings))
# print(sum(list_of_numbers))

d = {'day' : 22, 'month' : 6, 'year' : 2015}

print("||".join(d.keys()))
# Home work 12.5.11
person= {'name' : 'Ivan Petrov'}
person['age']= 25
person['email'] = 'ivan_petrov@example.com'
person['phone'] = '8(800)555-35-35'
print(person)

title = input("Введите название книги:")
author = input("Введите фамилию автора:")
year = int(input("Введите год издания:"))
print(title, author, year)
book = {'title' : title,
        'author' : author,
        'year' : year}
print(book)
title = "Алиса в стране чудес"
author = "Кэрролл"
year = int("1865")

book = {'title' : title,
        'author' : author,
        'year' : year}
print(book)

L= [1,2,1,3,2]
b=set(L)
c=list(set(L))
print(c)

#HW 12.5.12
text = input("Введите текст:")
unique = list(set(text))
print("Количество уникальных символов", len(unique))

numb1={2.0, 5.0, 35.0, 45.0, 54.0}
numb2={10.0, 25.0, 35.0, 45.0, 63.0}
numb=numb1.symmetric_difference(numb2)
print(numb)