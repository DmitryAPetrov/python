#--------------------------------Упражнение №1--------------------------------
# userTypes = [
#     1,
#     "userStr",
#     True, {1,2},
#     {1:3,},
#     [],
#     (1,),
# ]
# for userType in userTypes:
#     print(type(userType))
#--------------------------------Упражнение №2--------------------------------
# userList = input("Введи числа через запятую:  ")
# userList = userList.split(",")
#
# i = 0
# while i < len(userList[:-1]):
#     userList[i], userList[i+1] = userList[i+1], userList[i]
#     i += 2
# print(userList)
#--------------------------------Упражнение №3--------------------------------
#
# seasons_dict = {'Зима': (12, 1, 2),
#                 'Весна': (3, 4, 5),
#                 'Лето': (6, 7, 8),
#                 'Осень': (9, 10, 11),
#                 }
# seasons_list = ['Зима',
#                 'Весна',
#                 'Лето',
#                 'Осень',
#                 ]
#
# while True:
#     userMonth_num = int(input("Введите весяц:  "))
#     try:
#         userMonth_num = int(userMonth_num) #Пробуем преобразовать к числу
#         if 12 < userMonth_num or userMonth_num< 0:
#             print('Ошибка ввода: месяц не может быть больше 12 и меньше 0')
#             continue
#     except ValueError as e:
#         print('Ошибка ввода: введите число')
#         print(e)
#         continue
#
#     #вычисляем индекс времени года
#     season_idx = userMonth_num //3 % 4
#     print(seasons_list[season_idx])
#     #берем из списка индекс времени года
#
#     for key, value in seasons_dict.items():
#         if userMonth_num in value:
#             print(key)
#             break
#     break

#--------------------------------Упражнение №4--------------------------------
userStr = input("Введите строу:  \n")
userStr = userStr.split()
for idx, userWord in enumerate(userStr.split(''), 1):
    print(f"{idx}:{userWord if len(userWord) < 10 else userWord[:10]}")


