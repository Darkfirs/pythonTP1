def max_del(a,b):
    while b>0:
        a,b = b,a%b
    return a

def reduction(list_pair):
    re = max_del(list_pair[0],list_pair[1])
    return (list_pair[0]//re,list_pair[1]//re)

def calculation(n):
    answer = []
    for i in range(1,n+1):
        for j in range(i+1,n+1):
            pair = i,j
            res = reduction(pair)
            answer.append(res)
    return sorted(answer)

def speak():
    n = int(input(('Введите максимальный знаминатель для вывода дробей:')))
    print('Вот ваши дроби:')
    for i in range(len(calculation(n))):
        speak_ans = set(calculation(n)[i])
        print(speak_ans)


if __name__ == '__main__':
    speak()