#ввод пользователем элементов списка
user_str = input("Введите свою строку используя пробел: ")
user_word = []

#вывод каждого элемента с новой строки с порядковым номером
num = 1
for element in range(user_str.count(" ") + 1):
    user_word = user_str.split()
    if len(str(user_word)) <= 10:
        print("{}. {}" .format(num, user_word))
        num += 1
    else:
        print("{}. {}" .format(num, user_word [element] [0:10]))
        num += 1