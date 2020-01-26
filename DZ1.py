
##----------------------Задание №1----------------------
# nameUser = input("Введите свое имя:   ")
# surnameUser =input("Введите свою фамилию:  ")
# print(f"Добрый день {nameUser} {surnameUser}")

##----------------------Задание №2----------------------
# second = int(input("Введите длительность времени в секундах:  "))
# minute = second//60
# second = second - minute*60
#
# clock = minute//60
#
# minute = minute - clock*60
#
# print(f'Конвертация (чч:мм:сс) -  {clock}:{minute}:{second}')

# #----------------------Задание №3----------------------
#
# numberUser = input("Введите число:   ")
#
# n = numberUser
# nn = n + numberUser
# nnn = nn + numberUser
#
# result = int(n) + int(nn) + int(nnn)
# print(f"Cумму чисел n + nn + nnn = {result}")

# #----------------------Задание №4----------------------
userNumber = int(input("Введите число:   "))
bigNumber = 0
while userNumber:
    if userNumber % 10 > bigNumber:
         bigNumber = userNumber % 10
    userNumber //= 10
print(bigNumber)





















