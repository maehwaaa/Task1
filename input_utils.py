def ask_int(prompt, low, high):
    """Запрашивает у пользователя целое число в заданном диапазоне."""
    while True:
        try:
            value = int(input(prompt))
        except ValueError:
            print("Ошибка: введите целое число.")
            continue
        if low <= value <= high:
            return value
        print(f"Ошибка: число должно быть от {low} до {high}.")
