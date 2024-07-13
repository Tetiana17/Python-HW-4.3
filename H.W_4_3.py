import random
lst = [random.randint(0, 100) for i in range(random.randint(3, 10))]
print(lst)
#створюємо новий список з вибраними елементами: перший елемент, третій елемент, другий елемент з кінця
new_lst = [lst[0], lst[2], lst[-2]]
print(new_lst)





