L = ['a', 'b', 'c']
print(id(L))

L.append('d')
print(id(L))
a = 5
b = 3+2
print(a-b)

shopping_center = ("Галерея", "Санкт-Петербург", "Лиговский пр., 30", ["H&M", "Zara"])
list_id_before = id(shopping_center[-1])

shopping_center[-1].append("Uniqlo")
list_id_after = id(shopping_center[-1])
print(list_id_after == list_id_before)


money = int(input('Введите сумму вклада'))
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
deposit = []
for key in per_cent:
    deposit.append(per_cent[key] * money / 100)
max_deposit = max(deposit)
print(deposit)
print ("Максимальная сумма, которую вы можете заработать — " + str(max_deposit))


money = int(input('Введите сумму вклада'))
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
deposit = []
for value in per_cent:
    deposit.append(per_cent[value] * money / 100)
max_deposit = max(deposit)
print(deposit)
print ("Максимальная сумма, которую вы можете заработать — " + str(max_deposit))