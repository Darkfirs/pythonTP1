def findres():
    x = int(input('''Введите значение х для формулы:'''))
    res = (x**2+1)*(x**2+x)+1
    print(f'{x}^4+{x}^3+x^{2}+x+1 = {res}')

if __name__ == '__main__':
    findres()
