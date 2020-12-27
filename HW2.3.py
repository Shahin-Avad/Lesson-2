#Создание словаря и ключей
seasons_list = ['Зима', 'Весна', 'Лето', 'Осень']

seasons_dict = {1 : 'Зима', 2 : 'Весна', 3 : 'Лето', 4 : 'Осень'}


#Ввод месяца числом
month = int(input("Введите месяц в числовом порядке: "))

while not 0 < month < 13:
    month = int(input("Введите месяц в числовом порядке: "))

#вывод соответствуеющего сообщения на экран через список и через словарь соответственно
if month < 3 or month == 12:
    
    print(seasons_list[0])
    print(seasons_dict.get(1))
   
elif  3 <= month <= 5:
    
    print(seasons_list[2])
    print(seasons_dict.get(2))
    
elif 6 <= month <= 8:
    
    print(seasons_list[3])
    print(seasons_dict.get(3))
    
else:
    
    print(seasons_list[4])
    print(seasons_dict.get(4))
    
