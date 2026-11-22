a = int(input('Первое число: '))
d = str(input('Операция: '))
b = int(input('Второе число: '))

print('Ответ:', end=' ')
if d == '+':
    print(a + b)
elif d == '-':
    print(a - b)
elif d == '*':
    print(a * b)
elif d == '/':
    print(a / b)
else:
    print('!Повторите попытку!')