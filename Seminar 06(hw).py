# Задача №1. Сгенерируйте случайный список из чисел.
# Увеличьте значение каждого элемента на 10 и запишите в новый список.

# def rand_list(n):
#     from random import randint
#     some_list=[]
#     for i in range(n):
#         some_list.append(randint(1,10))
#     return some_list

# x=int(input('Введите количество элемнтов массива: '))
# s1=rand_list(x)
# print(s1)
# s2=list(map(lambda y: y+10, s1))
# print(s2)
#------------------------------------------------------

# Задача №2. Задан список возрастов некоторых людей. Выберите всех взрослых, возраст которых от 18 и больше, и выведите отдельным списком.
ages = [5, 12, 17, 18, 24, 32]
adults=list(filter(lambda x: x>=18, ages))
print(adults)
