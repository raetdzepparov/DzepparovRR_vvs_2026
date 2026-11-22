def sum(a,b): return a+b
def sub(a,b): return a-b
def mul(a,b): return a*b
def div(a,b): return a/b

a = int(input('Первое число: '))
d = str(input('Операция: '))
b = int(input('Второе число: '))

print('Ответ:', end=' ')
if d == '+':
    print(sum(a,b))
elif d == '-':
    print(sub(a,b))
elif d == '*':
    print(mul(a,b))
elif d == '/':
    print(div(a,b))
else:
    print('!Повторите попытку!')