#Создать функцию, которая будет случайным образом генерировать два списка случайным образом,
# после чего сравнивать элементы этих двух списков и выводить в консоль новый список, который будет состоять из элементов,
# которые есть в обоих оригинальных списках.
from random import randint
randoms1 = []
randoms2 = []
for i in range(10):
    randoms1.append(randint(0,15))
    randoms2.append(randint(0,15))
print(randoms1)
print(randoms2)


same_values = set(randoms1) & set(randoms2)
print(same_values)
