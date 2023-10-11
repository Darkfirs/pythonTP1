import os
from sys import argv

def check_files(file1,file2):
    if os.path.isfile(f'{file1}') and not(os.path.isfile(f'{file2}')):
        return True
    elif os.path.isfile(f'{file2}'):
        print('Файл g существует')
        return False
    elif not(os.path.isfile(f'{file1}')):
        print('Нет файла f')
        return False


def open_find(a,b,f1):
    first = []
    second = []
    third = []
    with open(f'{f1}','r')as file:
        all_num = file.read().split()
        for i in range(len(all_num)):
            if int(all_num[i])<a:
                first.append(int(all_num[i]))
            if a<int(all_num[i])<b:
                second.append(int(all_num[i]))
            if int(all_num[i])>b:
                third.append(int(all_num[i]))
    return first,second,third


def write_new(group1,group2,group3,f2):
    with open(f'{f2}','w')as file:
        for i in range(len(group1)):
            file.write(str(group1[i])+' ')
        file.write('\n')
        for g in range(len(group2)):
            file.write(str(group2[g])+' ')
        file.write('\n')
        for j in range(len(group3)):
            file.write(str(group3[j])+' ')


def main(a,b,f1,f2):
    if check_files(f1,f2):
        g1,g2,g3 = open_find(a,b,f1)
        write_new(g1,g2,g3,f2)
    else:
        print('Ошибка в файлах')



if __name__ == '__main__':
    a, b, file_in, file_out = argv
    main(int(a), int(b), file_in, file_out)