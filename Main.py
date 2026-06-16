from datetime import date

from date_utils import (
    calculate_age,
    day_of_week,
    days_in_month,
    is_leap_year,
)
from display import print_date_as_stars
from input_utils import ask_int


def main():
    print("Введите дату вашего рождения.")
    while True:
        day = ask_int("День (1-31): ", 1, 31)
        month = ask_int("Месяц (1-12): ", 1, 12)
        year = ask_int(f"Год (1900-{date.today().year}): ",
                       1900, date.today().year)
        if day <= days_in_month(month, year):
            break
        print(f"Ошибка: в {month:02d}.{year} только "
              f"{days_in_month(month, year)} дней. Введите дату заново.")

    print()
    print(f"Вы родились в день недели: {day_of_week(day, month, year)}")

    if is_leap_year(year):
        print(f"{year} год — високосный.")
    else:
        print(f"{year} год — не високосный.")

    print(f"Сейчас вам полных лет: {calculate_age(day, month, year)}")

    print()
    print("Ваша дата рождения на электронном табло:")
    print_date_as_stars(day, month, year)


if __name__ == "__main__":
    main()
