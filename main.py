import json
import locale
import os
import time

locale.setlocale(locale.LC_ALL, "sl_SI.UTF-8")

file_path = "data_task2_2.json"

if not os.path.exists(file_path):
        raise FileNotFoundError(f"{file_path} does not exist!")
try:
    with open(file_path, "r") as car_data_file:
        car_data = json.load(car_data_file)

    file = open("rich_honda_owners.txt", "w")

    for person in car_data:
        try:
            car_make = person["car_make"].lower()
            if car_make == "honda":
                if person["bank"][0] == "$" and float(person["bank"][1:]) > 5000:
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
                else:
                    print(
                        "Attribute value is incomplete ($ sign missing from bank property)"
                    )
        except KeyError as e:
            print(f"Record doesn't contain {e} attribute.")
    file.close()
except json.decoder.JSONDecodeError:
    raise ValueError(f"{file_path} has corrupt JSON structure!")
