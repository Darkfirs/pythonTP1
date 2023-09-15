def findres(x):
    res = (x**2+1)*(x**2+x)+1
    ans = f'{x}^4+{x}^3+x^{2}+x+1 = {res}'
    return ans

if __name__ == '__main__':
    x = int(input('''Введите значение х для формулы:'''))
    print(findres(x))
