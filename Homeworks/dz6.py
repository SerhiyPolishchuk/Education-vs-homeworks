import random

spisok = [random.randint(0,10) for i in range(10)]
print(spisok)

iskaemoe = int(input("Введите искаемое число: "))
indeks = spisok.index(iskaemoe)

print("Число " + str(iskaemoe) + " в списке под номером " + str(indeks))

