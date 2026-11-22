class Calc:
    def calc(self, a, b, d):
        if d == '+':
            return a+b
        elif d == '-':
            return a-b
        elif d == '*':
            return a*b
        else:
            return a/b

calc = Calc()
while True:
    try:
        a = int(input('Первое число: '))
    except ValueError:
        print('Нужно число!')
        break
    d = str(input('Операция: '))
    try:
        b = int(input('Второе число: '))
    except ValueError:
        print('Нужно число!')
        break
    if d == '/' and b == 0:
        print('Чёто не то делаешь')
    elif d in ('+', '-', '*', '/'):
        print('Ответ:', calc.calc(a,b,d))
    else:
        print('Введены неверные значения!')
    pr = str(input('Продолжить? '))
    if pr.lower() == 'no':
        break