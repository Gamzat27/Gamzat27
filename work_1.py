
def add_everything_up(a, b):
    try:
        # Пытаемся сложить a и b
        return a + b
    except TypeError:
        # Если возникла ошибка при сложении (разные типы), объединяем их в строку
        return str(a) + str(b)


print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))
print(add_everything_up(22, 55))
print(add_everything_up('string', 'string'))