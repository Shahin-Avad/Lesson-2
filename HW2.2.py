
#создаем список через функцию input с выводом на экран
num = int(input("Сколько элементов будет в вашем списке? "))

while not num > 0:  
    num = int(input("Сколько элементов будет в вашем списке? "))

some_list = []

i=0
while i < num:
    some_list.append(input("Элемент вашего списка: "))
    i += 1

print("Список: ", some_list)

#меняем местами эелементы с выводом конечного результатана экран
for i in range(int(len(some_list)/2)):
        some_list[i], some_list[i + 1] = some_list[i + 1], some_list[i]
        i += 2
print("Измененный список: ", some_list)