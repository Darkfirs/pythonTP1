import csv

def save_file(dict_words,file):
    with open(f'{file}','w')as file:
        file_writer = csv.writer(file, delimiter="=", lineterminator="\n")
        for i,g in  dict_words.items():
            c = i,g
            file_writer.writerow(c)
def main(file_int,file_out):
    dict = {}
    # words = []
    # words_count = []
    with open(f'{file_int}','r')as file:
        for line in file:
            sp_line = line.split()
            for i in range(len(sp_line)):
                if sp_line[i] not in dict:
                    dict[f'{sp_line[i]}']=0
                    # words.append(sp_line[i])
                    # words_count.append(0)
                if sp_line[i] in dict:
                    dict[f'{sp_line[i]}'] += 1
                    # c = words.index(sp_line[i])
                    # words_count[c] += 1
    save_file(dict,f'{file_out}')

if __name__ == '__main__':
    main('src.txt','dst.csv')


