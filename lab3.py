# №1
def greet(name):
    print(f'Привет, {name}!')


def square(number):
    return number ** 2

def max_of_two(a, b):
    if a > b:
        return a
    else:
        return b


greet("Кирюха")
greet('Катяэ')

print("Квадр 3:", square(3))
print("Квадр 7:",  square(7))

print("Больше из 2 и 26:", max_of_two(2, 26))
print("Больше из 37 и 15:", max_of_two(37, 15))

# №2
def calculate_rectangle(width, height):
    return width * height 

def calculate_perimeter(width, height):
    return 2 * (width + height)

def describe_rectangle(width, height, unit="см"):
    area = calculate_rectangle(width, height)
    perim = calculate_perimeter(width, height)

    print(f"Прямоугл {width}*{height}: S = {area} {unit}**2, P = {perim} {unit}")

describe_rectangle(3, 8) 
describe_rectangle(2, 10, unit="м") 

# №3
value = 10

def example():
    value = 20
    print("Внутр фнкц:", value)
    
    local_var = 9
    print("Другая локальная переменная:", local_var)

example()
print("Снаружи фнкц:", value)  

# №4
a = [1,12,13,14,2,4,17,23,24,8,7]
print("Начал список:", a)

print("первый элемент:", a[0])
print("третий элемент:", a[2])
print("последний элемент:", a[-1])

a[1] = 67
print("Изм 2 элм:", a)

a.append(52)
print("Добавление в список:", a)

a.remove(17)
print("Удаление 17 из списка:", a)

print("Итоговый список:", a)
print("Кол-во элементов:", len(a))

# №5
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Исходный список:", numbers)
print("Первые три:", numbers[:3])
print("Последние три:", numbers[-3:])
print("С 3 по 7:", numbers[2:7])
print("Каждый второй:", numbers[::2])
print("В обратном порядке:", numbers[::-1])

# №6
measurements = (1, 2, 3, 4, 5, 6, 7, 8, 9)
print("Исходный кортеж:", measurements)

print("Первый элемент:", measurements[0])
print("Последний элемент:", measurements[-1])
print("Несколько элементов:", measurements[3:6])

# measurements[2] = 15

a = measurements[0]
b =  measurements[1]
print(f"Распаковка: a = {a}, b = {b}")

c= list(measurements)
c[0] = 67
new_measurements = tuple(c)

print("Новый измененный кортеж:", new_measurements)

# №7
a = [1,12,13,14,2,4,17,23,24,8,7]
print("Исходный список:", a)

print("Кол-во элементов:", len(a))
print("Сумма элементов:", sum(a))
print("Минимальное значение:", min(a))
print("Максимальное значение:", max(a))

b = sum(a) / len(a)
print("Среднее арифметическое:", b)

sorted_c = sorted(a)
print("После sorted:", a)        
print("Отсортированная копия:", sorted_c) 

a.sort()
print("После sort:", a)

# №8
def calculate_sum(numbers):
    summm = 0
    for i in numbers:
        summm += i
    return summm

def find_min(numbers):
    minnn = numbers[0]
    for i in numbers:
        if i < minnn: 
            minnn = i
    return minnn

def find_max(numbers):
    maxxx = numbers[0]
    for i in numbers:
        if i > maxxx: 
            maxxx = i
    return maxxx

a = [14,2,4,12,11]
print("Список:", a)

print("Сумма:", calculate_sum(a), " Встроенная фк:", sum(a))
print("Минимум:", find_min(a), " Встроенная фк:", min(a))
print("Максимум:", find_max(a), " Встроенная фк:", max(a))


# №9
def find_element(numbers, target):
    for i in range(len(numbers)):
        if numbers[i] == target:
            return i
    return -1

a = [1,3,4,6,7,8,9]
print("Список для поиска:", a)

target_1 = 6
res_1 = find_element(a, target_1)
print(f"Ищем {target_1}: индексе {res_1}")

target_2 = 67
res_2 = find_element(a, target_2)
print(f"Ищем {target_2}: {res_2} (не найдено)")

# №10

def calculate_sum(numbers):
    summm = 0
    for i in numbers:
        summm += i
    return summm

def find_min(numbers):
    minnn = numbers[0]
    for i in numbers:
        if i < minnn: 
            minnn = i
    return minnn

def find_max(numbers):
    maxxx = numbers[0]
    for i in numbers:
        if i > maxxx: 
            maxxx = i
    return maxxx

def analyze(numbers):
    minnn = find_min(numbers)
    maxxx = find_max(numbers)
    average = calculate_sum(numbers) / len(numbers)
    return minnn, maxxx, average

a = [1,4,1,13,2,22]
mink, maxk, avgk= analyze(a)

print("Список:", a)
print(f"Минимум: {mink}")
print(f"Максимум: {maxk}")
print(f"Среднее: {avgk}")

#№11
numbers = [-10, 3, -2, 8, -5]
print("Исходный список:", numbers)

sorted_norm = sorted(numbers)
print("Обычная сортировка:", sorted_norm)

sorted_abs = sorted(numbers, key=lambda x: abs(x))
print("Сортировка по модулю:", sorted_abs)

#№12
def calculate_average(measurements):
    total = 0
    for x in measurements:
        total += x
    return total / len(measurements)

def find_minimum(measurements):
    minnn = measurements[0]
    for x in measurements:
        if x < minnn:
            minnn = x
    return minnn

def find_maximum(measurements):
    maxxx = measurements[0]
    for x in measurements:
        if x > maxxx:
            maxxx = x
    return maxxx

def count_above_average(measurements):
    avg = calculate_average(measurements)
    count = 0
    for x in measurements:
        if x > avg:
            count += 1
    return count

def find_value(measurements, target):
    for i in range(len(measurements)):
        if measurements[i] == target:
            return i
    return -1

def analyze_measurements(measurements):
    mink = find_minimum(measurements)
    maxk = find_maximum(measurements)
    avgk = calculate_average(measurements)
    return mink, maxk, avgk



a = [12,45,31,1,6,14,33,21]
min_m, max_m, avg_m = analyze_measurements(a)

print(f"Количество измерений: {len(a)}")
print(f"Минимальное значение: {min_m}")
print(f"Максимальное значение: {max_m}")
print(f"Среднее значение: {avg_m}") 
print(f"Количество значений выше среднего: {count_above_average(a)}")


target = 33
result = find_value(a, target)
if result != -1:
     print(f"Поиска значения {target}: найдено на индексе {result}")
else:
    print(f"Поиска значения {target}: не найдено (-1)")
    