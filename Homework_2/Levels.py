def level_1():
    test_str = "пРоГраМмИрОвАнИе_КруТо"
    print('\nДобро пожаловать на уровень 1! Данный уровень рассматривает 3 метода изменения регистра в строке:',
          '1) upper() - переводит все буквы в верхний регистр;',
          '2) lower() - переводит все буквы в нижний регистр;',
          '3) capitalize() - делает первую букву заглавной, остальные строчными.',
          '', f'Пример на строке "{test_str}":', sep='\n')

    print('upper():', test_str.upper())
    print('lower():', test_str.lower())
    print('capitalize():', test_str.capitalize())

    print('\nВведите номер метода, который хотите реализовать:')
    try:
        choice = int(input())
        if choice not in (1, 2, 3):
            print('Данные некорректны!')
            return

        user_str = input('Введите строку: ')
        # Используем словарь для вызова метода, чтобы избежать множества if-elif
        methods = {1: str.upper, 2: str.lower, 3: str.capitalize}
        print('Результат:', methods[choice](user_str))
    except ValueError:
        print('Данные некорректны!')


def level_2():
    test_str = "Питон это мощь. Очень мощь"
    print('\nДобро пожаловать на уровень 2! Данный уровень рассматривает 3 метода работы с подстроками:',
          '1) find(подстрока) - ищет индекс первого вхождения (или -1);',
          '2) replace(старое, новое, кол-во) - заменяет подстроки;',
          '3) count(подстрока) - считает количество непересекающихся вхождений.',
          '', f'Пример на строке "{test_str}":', sep='\n')

    print('find("мощь"):', test_str.find('мощь'))
    print('replace("мощь", "сила"):', test_str.replace('мощь', 'сила'))
    print('count("о"):', test_str.count('о'))

    print('\nВведите номер метода, который хотите реализовать:')
    try:
        choice = int(input())
        if choice not in (1, 2, 3):
            print('Данные некорректны!')
            return

        if choice == 1:
            s = input('Введите исходную строку: ')
            sub = input('Введите искомую подстроку: ')
            print('Результат:', s.find(sub))
        elif choice == 2:
            s = input('Введите исходную строку: ')
            old = input('Введите подстроку для замены: ')
            new = input('Введите новую подстроку: ')
            k = int(input('Введите кол-во замен (или -1 для всех): '))
            if k < -1:
                print('Данные некорректны!')
            elif k == -1:
                print('Результат:', s.replace(old, new))
            else:
                print('Результат:', s.replace(old, new, k))
        else:
            s = input('Введите исходную строку: ')
            sub = input('Введите искомую подстроку: ')
            print('Результат:', s.count(sub))
    except ValueError:
        print('Данные некорректны!')


def level_3():
    test_str = "red;green;blue"
    test_list = ['red', 'green', 'blue']
    print('\nДобро пожаловать на уровень 3! Данный уровень рассматривает методы разбиения и сборки строк:',
          '1) split(разделитель) - разбивает строку на список по разделителю;',
          '2) join(список) - собирает строку из списка с заданным разделителем.',
          '', f'Пример на строке "{test_str}":', sep='\n')

    print('split(";"):', test_str.split(';'))
    print(f'\nПример на списке {test_list}:', sep='\n')
    print('join("-"):', '-'.join(test_list))

    print('\nВведите номер метода, который хотите реализовать:')
    try:
        choice = int(input())
        if choice not in (1, 2):
            print('Данные некорректны!')
            return

        if choice == 1:
            s = input('Введите исходную строку: ')
            sep = input('Введите разделитель (пробел тоже нужно ввести!): ')
            print('Результат:', s.split(sep))
        else:
            k = int(input('Введите количество элементов списка: '))
            if k < 1:
                print('Данные некорректны!')
                return
            print('Теперь по одному вводите каждый элемент:')
            # Используем генератор списка для более компактного кода
            arr = [input() for _ in range(k)]
            sep = input('Введите разделитель (может быть пустым): ')
            print('Результат:', sep.join(arr))
    except ValueError:
        print('Данные некорректны!')


def level_4():
    test_str1 = "9876!@#"
    test_str2 = "   data_science   "
    print('\nДобро пожаловать на уровень 4! Данный уровень рассматривает методы проверки и очистки строки:',
          '1) isdigit() - True, если строка состоит только из цифр;',
          '2) isalpha() - True, если строка состоит только из букв;',
          '3) strip(символы) - удаляет указанные символы (или пробелы) по краям.',
          '', f'Пример на строке "{test_str1}":', sep='\n')

    print('isdigit():', test_str1.isdigit())
    print('isalpha():', test_str1.isalpha())
    print(f'\nПример на строке "{test_str2}":', sep='\n')
    print('strip():', test_str2.strip())

    print('\nВведите номер метода, который хотите реализовать:')
    try:
        choice = int(input())
        if choice not in (1, 2, 3):
            print('Данные некорректны!')
            return

        if choice == 1:
            s = input('Введите строку: ')
            print('Результат:', s.isdigit())
        elif choice == 2:
            s = input('Введите строку: ')
            print('Результат:', s.isalpha())
        else:
            s = input('Введите исходную строку: ')
            chars = input('Введите убираемые символы строкой (пробел тоже нужно ввести!): ')
            print('Результат:', s.strip(chars))
    except ValueError:
        print('Данные некорректны!')


def fix_string(text):
    """Улучшенная читаемость функции форматирования при сохранении оригинальной логики"""
    text = text.strip()
    if not text:
        return text
    while '  ' in text:
        text = text.replace('  ', ' ')
    for punct in ('.', ',', ':', ';', '!', '?'):
        text = text.replace(f' {punct}', punct)
    for punct in ('.', ',', ':', ';', '!', '?'):
        text = text.replace(f'{punct} ', punct).replace(punct, f'{punct} ')

    text = text.rstrip()

    text = text.capitalize()

    result = []
    for i, char in enumerate(text):
        if i >= 2 and text[i - 2] in '.!?' and text[i - 1] == ' ':
            result.append(char.upper())
        else:
            result.append(char)

    return ''.join(result)


def level_5():
    test_str = "        pYtHon;is.AWESome     "
    print('\nДобро пожаловать на уровень 5!',
          'Данный уровень превращает заданную строку в нормальный вид, используя методы из предыдущих уровней.',
          '', f'Пример на строке "{test_str}":', sep='\n')

    print(fix_string(test_str))

    print('\nВведите строку, которую хотите исправить:')
    user_text = input()
    print('Результат:', fix_string(user_text))


levels = {
    1: level_1,
    2: level_2,
    3: level_3,
    4: level_4,
    5: level_5
}

while True:
    try:
        x = int(input('Введите номер уровня: '))
    except ValueError:
        print('Данные некорректны!')
        continue

    if x in levels:
        levels[x]()
    else:
        print('Такого уровня не существует!')

    if input('Продолжить? Введите "да" или "нет": ').strip().lower() == 'нет':
        break

