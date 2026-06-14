def is_year_leap(year):
    """Возвращает True, если год високосный, иначе False."""
    return year % 4 == 0

# Вызов функции для примера
    year = 2024
    result = is_year_leap(year)
    print(f"год {year}: {result}")

# Дополнительная проверка
    year2 = 2023
    print(f"год {year2}: {is_year_leap(year2)}")
