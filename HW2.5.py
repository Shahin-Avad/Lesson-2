#Вывод списка на экран
my_list = [7, 5, 3, 3, 2]
print("Рейтинг - {}" .format(my_list))

#Вводим произвольный элемент для внесения в список 
element = int(input("Введите число или 2020 для выхода: "))

#Начало цикла
while element != 2020:
    for number_element in range(len(my_list)):
        
        #условие когда вводимый элемент равен элементу под номер 'number_element' в списке 'my_list'
        #добавление элемента в список на позицию 'number_element + 1' после найденного элемента
        if my_list[number_element] == element:
            my_list.insert(number_element + 1, element)
            break
        
        #условие когда вводимый элемент больше первого элемента(нулевого элемента)
        #добавление элемента на позицию нулевого элемента(НЕ ЗАМЕНА, А СДВИГ)
        elif my_list[0] < element:
            my_list.insert(0, element)
        
        #условие когда элемент меньше последнего эелемента
        #добавление элемента на позицию последнего элемента
        elif my_list[-1] > element:
            my_list.append(element)
        
        
        #условие когда элемент находит в диапозоне между двумя числами 
        #например, 19 находится между 7 и 24 в списке [24, 7,...]
        #элемент добавляется между двумя такими элементами 
        elif my_list[number_element + 1] < element < my_list[number_element]:
            my_list.insert(number_element + 1, element)
            break
    #новый цикл
    print("Текущий список - {}" .format(my_list))
    element = int(input("Введите число "))

#сообщение о выходе
print("Вы вышли")