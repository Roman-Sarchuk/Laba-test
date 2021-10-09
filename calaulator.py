a = float(input('Ведіть число: '))
c = input('Ведіть дію: ')
b = float(input('Ведіть число: '))

if c == '+':
    print('Результат:', a + b)
elif c == '-':
    print('Результат:', a - b)
elif c == '*':
    print('Результат:', a * b)
elif c == '/':
    if b != 0:
        print('Результат:', a / b)
    else:
        print('На нуль ділити не можна!')
elif c == '**':
    print('Результат:', a ** b)
elif c == '//':
    print('Результат:', a // b)
elif c == '%':
    print('Результат:', a % b)
else:
    print('Неправильний знак...')


