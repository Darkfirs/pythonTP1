from MergeSort import *


def main():
    try:
        input_array = input("Введите элементы через пробел: ").split()
        for i in range(len(input_array)):
            if input_array[i].isdigit():
                input_array[i] = int(input_array[i])

        sorted_array = merge_sort(input_array)

        print("Отсортированный массив:", sorted_array)
    except TypeError:
        print("Ошибка: Введите элементы одного типа.")


if __name__ == "__main__":
    main()
