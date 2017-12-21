import math

def print_delimiter(symbol='+', num_repeat=40):
    print(symbol*num_repeat)


def power(base, exp):
    print('power func')
    return base**exp


def pretty_print(value):
    print_delimiter()
    print('Value:', value)
    print_delimiter('~', 45)


result1 = (power(2, 5))
pretty_print(result1)


def rectangle_square(width, height):
    result = width * height
    return result


my_pi = math.pi
result2 = rectangle_square(10, 20)
pretty_print(result2)


def circle_square(radius):
    result = power(radius, 2) * my_pi
    return result


result3 = (circle_square(10))
pretty_print(result3)


def calculate_sum_and_product(a, b):
    sum_result = a+b
    product_result = a*b
    return sum_result, product_result


result4, result5 = calculate_sum_and_product(2, 3)
pretty_print(result4)
pretty_print(result5)


def faren2celc(degrees):
    return (degrees - 32) / 1.8


def celc2faren(degrees):
    return degrees * 1.8 + 32


celc96 = faren2celc(96)
print(celc96)
print(celc2faren(36.6))


def kelv2celc(degrees):
    return degrees - 273.15


print(kelv2celc(293.15))
