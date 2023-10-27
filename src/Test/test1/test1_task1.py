import os
import sys

def check_files(file1, file2):
    if os.path.isfile(f"{file1}") and not (os.path.isfile(f"{file2}")):
        return True
    elif os.path.isfile(f"{file2}"):
        print("Файл g существует")
        return False
    elif not (os.path.isfile(f"{file1}")):
        print("Нет файла f")
        return False


def save_words(file2, dict_words):
    with open(file2, "w") as file:
        for i, g in dict_words.items():
            c = f"{i} = {g} \n"
            file.write(c)


def open_find(file1):
    dict = {}
    all_letter = ""
    with open(file1, "r") as file:
        for line in file:
            let = line.split()
            for g in range(len(let)):
                all_letter += let[g]
            for i in range(len(all_letter)):
                if "A" <= all_letter[i] <= "Z" or "a" <= all_letter[i] <= "z":
                    if not all_letter[i] in dict:
                        dict[f"{all_letter[i]}"] = 1
                    else:
                        dict[f"{all_letter[i]}"] += 1

    res = {k: v for k, v in sorted(dict.items(), key=lambda item: item[1])}
    return res


def main(f1, f2):
    if check_files(f1, f2):
        save_words(f2, open_find(f1))


if __name__ == "__main__":
    file1, file2 = sys.argv[1], sys.argv[2]
    main(file1, file2)
