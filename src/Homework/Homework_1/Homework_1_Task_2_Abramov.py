import math as m

def scalar_product(a,b):
    res = 0
    for i in range(len(a)):
        res += a[i] * b[i]
    return res
def length(a):
    sum = 0
    for i in range(len(a)):
        if a[i] != 0:
            sum += a[i] ** 2
    res = sum ** 0.5
    return res


def mat1():
    n,m = int(input('Введите количество строк:')), int(input('Введите количество столбцов:'))
    print('Вводите через пробел числа строки:')
    matrix = []
    for i in range(n):
        matrix.append(list(map(int,input().split())))
    tra_matrix =[[0 for j in range(len(matrix))] for i in range(len(matrix[0]))]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            tra_matrix[j][i] = matrix[i][j]
    for i in range(len(tra_matrix)):
        for j in range(len(tra_matrix[i])):
            print(tra_matrix[i][j], end=' ')
        print()



def mat2():
    n, m = int(input('Введите количество строк для 1-й матрицы:')), int(input('Введите количество столбцов для 1-й матрицы:'))
    print('Вводите через пробел числа строки для 1-й матрицы:')
    matrix_1 = []
    for i in range(n):
        matrix_1.append(list(map(int,input().split())))
    a,b = int(input('Введите количество строк для 2-й матрицы:')), int(input('Введите количество столбцов для 2-й матрицы:'))
    print('Вводите через пробел числа строки для 2-й матрицы:')
    matrix_2 = []
    for i in range(a):
        matrix_2.append(list(map(int,input().split())))

    res_mat = [[matrix_1[i][j] + matrix_2[i][j] for j in range
    (len(matrix_1[0]))] for i in range(len(matrix_1))]
    for x in res_mat:
        print(x)
def mat3():
    n, m = int(input('Введите количество строк для 1-й матрицы:')), int(
        input('Введите количество столбцов для 1-й матрицы:'))
    print('Вводите через пробел числа строки для 1-й матрицы:')
    matrix_1 = []
    for i in range(n):
        matrix_1.append(list(map(int, input().split())))
    a, b = int(input('Введите количество строк для 2-й матрицы:')), int(
        input('Введите количество столбцов для 2-й матрицы:'))
    print('Вводите через пробел числа строки для 2-й матрицы:')
    matrix_2 = []
    for i in range(a):
        matrix_2.append(list(map(int, input().split())))
    matrix_void = [[0 for x in range(n)] for y in range(m)]

    for i in range(len(matrix_1)):
        for j in range(len(matrix_2[0])):
            for k in range(len(matrix_2)):
                matrix_void[i][j] +=(matrix_1[i][k] * matrix_2[k][j])
    for x in matrix_void:
        print(x)
def matsp():
    choice = int(input('''Что именно вы хотите сделать?
        1.Транспонировать
        2.Сложить
        3.Найти произведение
        :'''))
    if choice == 1:
        mat1()
    if choice == 2:
        mat2()
    if choice == 3:
        mat3()

def vek1():
    vek_a = list(map(int,input('Введите значения вектора a через пробел: ').split()))
    vek_b = list(map(int,input('Введите значения вектора b через пробел: ').split()))
    if len(vek_b)!= len(vek_a):
        print('Ошибка, размерность векторов не совпадает')
    else:
        print('Результат скалярного произведения равен: ',scalar_product(vek_a,vek_b))


def vek2():
    vek_a = list(map(int, input('Введите значения вектора a через пробел: ').split()))
    print('Длинная вектора а равна', length(vek_a))
def vek3():
    vek_a = list(map(int, input('Введите значения вектора a через пробел: ').split()))
    vek_b = list(map(int, input('Введите значения вектора b через пробел: ').split()))
    rr = scalar_product(vek_a,vek_b)/round(length(vek_a)*length(vek_b))

    print(f'Угол между векторами примерно равен:',round(m.degrees(m.acos(rr))))


def veksp():
    choice = int(input('''Что именно вы хотите сделать?
    1.Найти скалярное произведение
    2.Вычислить длину
    3.Найти угол между ними
    :'''))
    if choice == 1:
        vek1()
    if choice == 2:
        vek2()
    if choice == 3:
        vek3()


def start():
    choice = int(input('Вы хотите работать с векторами(1) или матрицами(2)(введите только число): '))
    if choice == 1:
        veksp()
    if choice == 2:
        matsp()

if __name__ == '__main__':
    start()