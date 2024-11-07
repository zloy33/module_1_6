# работа со словарями

my_dict = {"Artem":1991,"Marina":1994,"Kazimir":1990} # словарь
print(my_dict)
print(my_dict["Marina"]) # Вывод значения по существующему ключу
print(my_dict.get("Polina")) # Вывод значения по несуществующему ключу
my_dict.update({"Inna":1971,
                "Denis":2002}) # добавление нескольких пар к словарю
name = my_dict.pop("Kazimir") # извлечение из словаря существующей пары
print(name) # вывод значения извлеченной пары из словаря
print(my_dict)

# работа с множествами

my_set = { 9,9,9,"qwerty",113.11,8,8,"qwerty", 113.11} # множество
print(my_set)
a_ = (my_set.update({"asdf",(12.2,13.3)})) # добавить несколько элементов
b_ = (my_set.discard(9)) # удалить элемент
print(my_set)