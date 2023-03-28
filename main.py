import json
import locale
import os
import sys

locale.setlocale(locale.LC_ALL, "sl_SI.UTF-8")
input_file_path = ""


def write_rich_honda_owners(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"{file_path} does not exist!")
    try:
        with open(file_path, "r") as car_data_file:
            car_data = json.load(car_data_file)

        file = open("rich_honda_owners.txt", "w")
        print("Parsing...")
        for person in car_data:
            try:
                car_make = person["car_make"].lower()
                if car_make == "honda":
                    if person["bank"][0] == "$":
                        if float(person["bank"][1:]) > 5000:
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
                            f"Attribute value is incomplete ($ sign missing from bank property)"
                        )
            except KeyError as e:
                print(f"Record doesn't contain {e} attribute.")
        print("OK")
        file.close()
    except json.decoder.JSONDecodeError as e:
        raise ValueError(f"{file_path} has corrupt JSON structure: {e}")


is_run_again = True
if len(sys.argv) == 2:
    input_file_path = sys.argv[1]


while is_run_again:
    try:
        if input_file_path == "":
            input_file_path = input("Path to JSON input file: ")
        write_rich_honda_owners(input_file_path)
        print(f'Output: {os.path.abspath("rich_honda_owners.txt")}')
        is_run_again = False
    except FileNotFoundError:
        print(
            "ERROR: File provided as script parameter does not exist. Provide another file!"
        )
        input_file_path = ""
    except ValueError as e:
        print(f"ERROR: {e}. Fix file before running script again!")
        input_file_path = ""

    except Exception as e:
        print(f"ERROR: {e}")
        input_file_path = ""
