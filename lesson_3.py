"""-------------------------------1-------------------------------
Реализовать функцию, принимающую два числа (позиционные аргументы)
и выполняющую их деление. Числа запрашивать у пользователя, предусмотреть
ситуации деления на ноль.
"""

# a = int(input('Введите числа которое будите делить'))
# b = int(input('Введите числа на которое будите делить'))
#
#
# def my_del(a, b: int) -> int:
#     if b == 0:
#         print('Вы на ноль делить нельзя')
#     else:
#         return a / b
# print(my_del(a, b))


"""-------------------------------2-------------------------------
Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
 имя, фамилия, год рождения, город проживания, email, телефон. Функция должна принимать
параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой
"""
#
# def user_inf(name: str, surname: str, year: int, city: str, email: str, phone: int):
#    """
#    Отображает данные о пользлвателе на экране
#    :param name: str
#    :param surname: str
#    :param year: int
#    :param city: str
#    :param email: str
#    :param phone: int
#    """
#    return f"{name} {surname},родившийся в {year}году, в городе {city}. Контакты {email}   {phone}"
#
# print(user_inf("Dmitry", "Petrov", 1991, "Nerehta", "p.dm.an@ya.ru", 89660000))


"""-------------------------------3-------------------------------
Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
"""
# def my_func(a: int, b: int, c: int, ) -> int:
#     return  max(a+b, b+c, c+a)
# print(my_func(1, 2, 3))

"""-------------------------------4-------------------------------
Программа принимает действительное положительное число x и целое отрицательное число y.
Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать в 
виде функции my_func(x, y). При решении задания необходимо обойтись без встроенной функции
возведения числа в степень.
"""
# def insert_sam(*args):
#     result = 0
#     exit_flag = False
#     for itm in args:
#         try:
#             result += float(itm) if itm else 0
#         except  ValueError as e:
#             if itm == 'q':
#                 exit_flag = not exit_flag
#     return result, exit_flag
#
# user_sam = 0
# while True:
#     user_input = input('Введи число через пробел\n').split(' ')
#     result_suum = user_exit = insert_sam(*user_input)
#     user_sam += result_suum
#     print(user_sam)
#
#     if user_exit:
#         print('buy')
#         break