# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

def day_of_week():
    day = int(input("Enter your day of week: "))
    if day == 6 or day == 7:
        return print("Yes")
    else:
        return print("No")    

day_of_week()        

# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

def logical_statement(x, y, z):
    print(f"¬({x} ⋁ {y} ⋁ {z}) = ¬{x} ⋀ ¬{y} ⋀ ¬{z} is {(not (x or y or z)) == (not x and not y and not z)}")
    return (not (x or y or z)) == (not x and not y and not z)

if (logical_statement(0, 0, 0) and logical_statement(0, 0, 1) and logical_statement(0, 1, 0) and 
logical_statement(0, 1, 1) and logical_statement(1, 0, 0) and logical_statement(1, 0, 1) and
logical_statement(1, 1, 0) and logical_statement(1, 1, 1)):
    print("True")
else:
    print("False")

# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

# Пример:

# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 ->  

x = int(input('Enter coordinate - x: '))
y = int(input('Enter coordinate - y: '))

def fined_quarter(x, y):
    if  x > 0 and y > 0:
        print(f'Point({x}, {y}) is located in 1 quarter  of the coordinate axis')
    elif x < 0 and y > 0:
        print(f'Point({x}, {y}) is located in 2 quarter  of the coordinate axis')    
    elif x < 0 and y < 0:
        print(f'Point({x}, {y}) is located in 3 quarter  of the coordinate axis')    
    elif x > 0 and y < 0:
        print(f'Point({x}, {y}) is located in 4 quarter  of the coordinate axis')

fined_quarter(x, y)

# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y)

quarter = int(input("Enter number of quarter of axis:  "))

def quarter_of_axis(quarter):
    if   quarter == 1: 
        return print(" The first axis: x from 0 to + ∞, y from 0 to + ∞") 
    elif quarter == 2: 
        return print(" The second axis: x from 0 to  - ∞, y from 0  to + ∞ ")  
    elif quarter == 3: 
        return print(" The third axis: x from 0 to  - ∞, y from 0  to - ∞ ")
    elif quarter == 4: 
        return print(" The four axis: x from 0 to  + ∞, y from 0  to - ∞ ")
    else:        
        return print("Error, try again")

quarter_of_axis(quarter)

# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

# Пример:

# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

x1 = int(input('Enter coordinate х1: '))
y1 = int(input('Enter coordinate y1: '))
x2 = int(input('Enter coordinate х2: '))
y2 = int(input('Enter coordinate y2: '))
import math
sqrt = round(math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2),2)
print(f'Distance: (A - ({x1}, {y1}) between B - ({x2}, {y2}) = {sqrt}')