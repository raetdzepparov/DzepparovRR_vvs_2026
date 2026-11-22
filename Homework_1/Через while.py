def dey(a,b, d):
    if d == '+':
        return(a + b)
    elif d == '-':
        return(a - b)
    elif d == '*':
        return(a * b)
    return(a / b)

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
        print('Ответ:', dey(a,b,d))
    else:
        print('Введены неверные значения!')
    pr = str(input('Продолжить? '))
    if pr.lower() == 'no':
        break