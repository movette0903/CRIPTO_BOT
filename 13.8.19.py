tickets = int(input('Введите количество билетов: '))
ages = []
for i in range(0, tickets):
    input_value = int(input(f'Введите возраст участника №{i + 1}:\n'))
    ages.append(input_value)
    def prise(age):
        if age < 18:
            return 0
        elif 18 <= age < 25:
            return 990
        else:
            return 1390
    full_prise = sum(map(prise, ages))
discount_prise = int(full_prise * 0.9)
if tickets > 3:
    print('Стоимость всех билетов со скидкой: ', discount_prise, "руб.")
else:
    print('Стоимость всех билетов: ', full_prise, "руб.")

