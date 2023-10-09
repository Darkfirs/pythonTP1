def res(a, b):
    c = 0
    n = 1
    while True:
        if b * n > a:
            break
        else:
            c = n
        n += 1
    q = a - b * c
    return c, q
    

def sear():
    a = int(input("Введите число а(делимое):"))
    b = int(input("Введите число b(делитель):"))

    print(f"Результат деления и остаток {res(a,b)}")
    # r=a-b*q

if __name__ == "__main__":
    sear()

