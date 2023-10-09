def search_ea(num):
    for i in range(2, round(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


if __name__ == "__main__":
    choi = int(input("Введите число-границу:"))
    b = []
    for i in range(1, choi):
        if search_ea(i):
            b.append(i)
    print(b)
