import random

def random_numbers():
    while True:
        k = 0
        random_number = random.randint(1000,9999)
        q = list(map(int,str(random_number)))
        for i in range(len(q)):
            if q.count(q[i])>1:
                k += 1
        if k == 0:
            break
    return random_number
def search(player_number):
    bulls = 0
    cows = 0
    cp_num = list(map(str,str(random_numbers())))
    pl_num = list(map(str,player_number))
    for i in range(len(cp_num)):
        if cp_num[i]==pl_num[i]:
            bulls += 1
        elif pl_num[i] in cp_num:
            cows += 1
    z = cp_num[0] + cp_num[1] + cp_num[2] + cp_num[3]
    return bulls,cows,z

def speak():
    player_choice = input('Введите 4 числа (без пробелa и без повторений):')
    print(f'У вас: {search(player_choice)[0]} быка, {search(player_choice)[1]} коровы (число компьютера: {search(player_choice)[2]})')

if __name__ == '__main__':
    speak()