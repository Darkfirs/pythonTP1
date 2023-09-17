def findres(x):
    z = x**2
    res = (z+1)*(z+x)+1
    ans = f'{x}^4+{x}^3+x^{2}+x+1 = {res}'
    return ans

if __name__ == '__main__':
    x = int(input('''Введите значение х для формулы:'''))
    print(findres(x))
