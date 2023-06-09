# Задача 30:  
# Заполните массив элементами арифметической прогрессии. 
# Её первый элемент, 
# разность и количество элементов нужно ввести с клавиатуры. 
# Формула для получения n-го члена прогрессии: 
# an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.
# Ввод: 7 2 5
# Вывод: 7 9 11 13 15

def arifmethic(n,end,step):
    arrey=[]
    for i in range(n,n+(end-1)*step+1,step):
        arrey.append(i)
    return arrey
   
n = int(input("First element "))
step = int(input("Step "))
end = int(input("Elements emmount  "))



