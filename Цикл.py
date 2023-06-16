S=0
N=5
for i in range(1, N+1):
    print("Значение суммы на предыдущем шаге: ", S)
    print("Текущее число:", i)
    S=S+i
    print("Значение суммы после сложения:",S)
    print("Текущее число:", i)

print("Конец цикла")
print()
print("Ответ:сумма равна =", S)
# 13.6.2
P=1
N=5
for i in range(1, N+1):
    P *=i
print(P)

# 13.6.3
N=5
for i in range(1, N+1):
    print("*" *i)

    #WHILE
S=0
n=1
while S<500:
    S+=n
    n+=1
    print("Ещё считаю ....")
print("Сумма равна:", S)
print("Количество чисел:", n)

n=1
while n ** 2 < 1000:
    n+=1
print("Квадат равен", n)

n=1
while True:
    print("Hello World")
    n += 1
    if n>10:
        break

n=1
while True:
    if n ** 2 >= 1000:
        print("Последние число", n-1)
        break
    n +=1

random_matrix = [
    [9, 2, 1],
    [2, 5, 3],
    [4, 8, 5]
]

min_value_rows = []  # здесь будут храниться минимальные значения для каждой строки
min_index_rows = []  # здесь будут храниться индексы минимальных значений для каждой строки
max_value_rows = []  # здесь будут храниться максимальные значения для каждой строки
max_index_rows = []  # здесь будут храниться индексы максимальных значений для каждой строки

for row in random_matrix:  # здесь мы целиком берем каждую сроку
    min_index = 0  # в качестве минимального значения возьмем первый элемент строки
    max_index = 0
    min_value = row[min_index]  # начальное минимальное значение для каждой строки будет новое
    max_value = row[max_index]  # для максимального значения тоже самое
    for index_col in range(len(row)):
        if row[index_col] < min_value:
            min_value = row[index_col]
            min_index = index_col
        if row[index_col] > max_value:
            max_value = row[index_col]
            max_index = index_col
    min_value_rows.append(min_value)
    min_index_rows.append(min_index)
    max_value_rows.append(max_value)
    max_index_rows.append(max_index)

print(min_value_rows)
print(min_index_rows)
print(max_value_rows)
print(max_index_rows)

N=2
M=3
matrix= [
    [0,1,2],
    [3,4,5],
]
for i in range (N):
    for j in range(M):
        print(matrix[i][j], end="")
    print()

list_=[-5,2,4,8,12,-7,5]

for i in range(len(list_)):
    print("Индекс элемента:", i )
    print("Значение элимента:", list_[i])
    print("---")
print("Конец цикла")

list_=[-5,2,4,8,12,-7,5]
for i, value in enumerate(list_):
    print("Индекс элемента:", i)
    print("Значение элемента:", value)
    print("---")
print("Конец цикла")