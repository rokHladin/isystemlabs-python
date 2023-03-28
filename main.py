import json
import locale
locale.setlocale(locale.LC_ALL, 'sl_SI.UTF-8')

with open("data_task1.json", "r") as car_data_file:
    car_data = json.load(car_data_file)

file = open("rich_honda_owners.txt", "w")

for person in car_data:
    if person["car_make"] == "Honda" and float(person["bank"][1:]) > 5000:
        bank_balance = float(person["bank"][1:])
        file.write(
            f'ID: {person["id"]}\n'
            f'Name: {person["first_name"]}\n'
            f'Surname: {person["last_name"]}\n'
            f'Email: {person["email"]}\n'
            f'Gender: {person["gender"]}\n'
            f'Bank state in USD: {locale.format_string("%.2f", bank_balance, grouping=True)}\n'
            "=====================================\n"
        )

file.close()
