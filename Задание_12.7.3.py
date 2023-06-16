money = int(input('Введите сумму вклада'))
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
deposit = []
for value in per_cent:
    deposit.append(per_cent[value] * money / 100)
max_deposit = max(deposit)
print(deposit)
print ("Максимальная сумма, которую вы можете заработать — " + str(max_deposit))