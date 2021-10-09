text = input('Ведіть текст: ')

print()

print('Результ: ', end='')
for i in reversed(text):
    print(i, end='')

print()
print()

print('Результат', text[::-1])