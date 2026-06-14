import math


def square(side):
    """Возвращает площадь квадрата. Сторона может быть дробной."""
    area = side * side
    # Если side не целое, округляем вверх
    if not isinstance(side, int):
        area = math.ceil(area)
    return area


print(square(5))     # 25
print(square(2.3))   # 5.29? Округляем вверх → 6
