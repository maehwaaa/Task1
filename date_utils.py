from datetime import date

WEEKDAYS = [
    "понедельник", "вторник", "среда", "четверг",
    "пятница", "суббота", "воскресенье",
]


def is_leap_year(year):
    """Определяет, является ли год високосным."""
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def day_of_week(day, month, year):
    """Возвращает название дня недели для заданной даты (формула Целлера)."""
    if month < 3:
        month += 12
        year -= 1
    k = year % 100
    j = year // 100
    h = (day + 13 * (month + 1) // 5 + k + k // 4 + j // 4 + 5 * j) % 7
    return WEEKDAYS[(h + 5) % 7]


def calculate_age(day, month, year):
    """Определяет, сколько сейчас полных лет пользователю."""
    today = date.today()
    age = today.year - year
    if (today.month, today.day) < (month, day):
        age -= 1
    return age


def days_in_month(month, year):
    """Возвращает количество дней в месяце с учётом високосного года."""
    days = [31, 29 if is_leap_year(year) else 28, 31, 30, 31, 30,
            31, 31, 30, 31, 30, 31]
    return days[month - 1]
