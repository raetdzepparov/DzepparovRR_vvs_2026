import pandas as pd
import numpy as np

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 200)


def get_age_stats(series):
    """Вспомогательная функция для сбора статистики по возрасту без дублирования кода."""
    return {
        'Среднее': round(series.mean(), 2),
        'Медиана': round(series.median(), 2),
        'Минимум': round(series.min(), 2),
        'Максимум': round(series.max(), 2),
        'Стд. отклонение': round(series.std(), 2),
        'Известных значений': int(series.count())
    }


def main():
    # 6
    print('#6')
    df = pd.read_csv('titanic.csv')
    print('Файл успешно загружен!\n')

    # 7
    print('#7')
    n = int(input('Введите n: '))
    print(f'Первые {n} строк(-и) таблицы:')
    print(df.head(n), '\n')

    # 8
    print('#8')
    print('Последние 5 строк таблицы:')
    print(df.tail(5), '\n')

    # 9
    print('#9')
    print(f'Строк и столбцов: {df.shape}\n')

    # 10
    print('#10')
    print(f'Столбцы: {df.columns.tolist()}\n')

    # 11
    print('#11')
    print('Типы данных:')
    print(df.dtypes, '\n')

    # 12
    print('#12')
    numer = ['PassengerId', 'Age', 'SibSp', 'Parch', 'Fare']
    categ = ['Survived', 'Pclass', 'Name', 'Sex', 'Ticket', 'Cabin', 'Embarked']
    print(f'Числовые признаки: {numer}')
    print(f'Категориальные признаки: {categ}\n')

    # 13
    print('#13')
    stats = df[numer].describe().T
    stats['median'] = df[numer].median()
    print('Статистика числовых признаков:')
    print(stats[['mean', 'median', 'min', 'max', 'std']].round(2), '\n')

    # 14
    print('#14')
    print('Количество пассажиров каждого класса:')
    print(df['Pclass'].value_counts().sort_index(), '\n')

    # 15
    print('#15')
    print(f"Количество уникальных значений в Embarked: {df['Embarked'].nunique()}\n")

    '''Контрольный вопрос:
    Числа 1, 2, 3 - это коды категорий (класс каюты), а не измеряемая величина.
    Между ними нет арифметического смысла (нельзя сказать, что 1-й класс "в 3 раза меньше" 3-го).
    Поэтому Pclass - категориальный признак.'''

    shape_before = df.shape

    # 16
    print('#16')
    print('Количество пропусков в каждом столбце:')
    print(df.isna().sum(), '\n')

    # 17
    print('#17')
    print('Процент пропусков относительно общего числа строк:')
    print((df.isna().mean() * 100).round(2), '\n')

    # 18
    print('#18')
    print(f"Максимум пропусков в: {df.isna().sum().idxmax()}\n")

    # 19
    print('#19')
    age_before = get_age_stats(df['Age'])
    print('Статистика Age до заполнения:')
    for k, v in age_before.items():
        print(f"  {k}: {v}")
    print()

    # 20
    print('#20')
    median_age = df['Age'].median()
    df['Age'] = df['Age'].fillna(median_age)
    print(f'Пропуски в Age заполнены медианой ({median_age})\n')

    # 21
    print('#21')
    age_after = get_age_stats(df['Age'])
    print('Статистика Age после заполнения:')
    for k, v in age_after.items():
        print(f"  {k}: {v}")
    print()

    # 22
    print('#22')
    comparison = pd.DataFrame({'До обработки': age_before, 'После обработки': age_after})
    print('Сравнительная таблица:')
    print(comparison, '\n')

    # 23
    print('#23')
    df = df.dropna(subset=['Embarked'])
    print('Все строки без Embarked удалены\n')

    # 24
    print('#24')
    cabin_missing_share = df['Cabin'].isna().mean()
    print(f"Доля пропусков в Cabin: {round(cabin_missing_share * 100, 2)}%")
    if cabin_missing_share > 0.5:
        df = df.drop(columns=['Cabin'])
        print('Столбец Cabin удалён, так как доля пропусков превысила 50%\n')

    # 25
    print('#25')
    print('Оставшиеся пропуски:')
    print(df.isna().sum(), '\n')

    # 26
    print('#26')
    print(f'Размер до обработки: {shape_before}')
    print(f'Размер после обработки: {df.shape}\n')

    '''Контрольные вопросы:
    #27. Медиана более устойчива к выбросам и сильной асимметрии распределения.
    А среднее «тянется» к выбросам, которых в Age достаточно.
    #28. Не изменились: медиана, минимум, максимум.
    Изменились: стандартное отклонение (уменьшилось), кол-во известных значений (стало равно числу строк).
    Визуально среднее не изменилось из-за округления, но на самом деле немного сдвинулось к медиане.
    #29. Все добавленные значения равны медиане, поэтому они сжимают разброс.
    Таким образом они уменьшают стандартное отклонение.
    #30. Нет, распределение искажается, так как появляется искусственный «пик» на медиане.
    Заполнение медианой не восстанавливает исходную форму распределения.'''

    # 31
    print('#31')
    survived_arr = df['Survived'].to_numpy()
    print(f"Общий процент выживших: {round(survived_arr.mean() * 100, 2)}%\n")

    # 32
    print('#32')
    sex_arr = df['Sex'].to_numpy()
    for sex in ['male', 'female']:
        mask = (sex_arr == sex)
        rate = round(survived_arr[mask].mean() * 100, 2)
        print(f"Процент выживших среди {sex}: {rate}%")
    print()

    # 33
    print('#33')
    age_arr = df['Age'].to_numpy()
    for sex in ['male', 'female']:
        mask = (sex_arr == sex)
        print(f"Средний возраст {sex}: {round(age_arr[mask].mean(), 2)}")
    print()

    # 34
    print('#34')
    for sex in ['male', 'female']:
        for s in [0, 1]:
            mask = (sex_arr == sex) & (survived_arr == s)
            label = 'выживших' if s == 1 else 'погибших'
            ages_in_group = age_arr[mask]

            if len(ages_in_group) > 0:
                print(f"Среди {sex} {label}: {round(ages_in_group.mean(), 2)}")
            else:
                print(f"Среди {sex} {label}: нет данных (0 человек)")
    print()

    # 35
    print('#35')
    print(f"Минимальная стоимость билета: {round(df['Fare'].min(), 2)}")
    print(f"Максимальная стоимость билета: {round(df['Fare'].max(), 2)}")
    print(f"Средняя стоимость билета: {round(df['Fare'].mean(), 2)}\n")

    # 36
    print('#36')
    print(f"Стандартное отклонение возраста: {round(age_arr.std(), 2)}\n")

    # Сравнительная таблица по полу
    data = {
        'Мужчины': ['0.0%', '29.52', 'нет данных (0 чел.)', '29.52'],
        'Женщины': ['100.0%', '29.73', '29.73', 'нет данных (0 чел.)']
    }
    index = ['Процент выживших', 'Средний возраст', 'Ср. возраст выживших', 'Ср. возраст погибших']
    comparative_df = pd.DataFrame(data, index=index)

    print('Сравнительная таблица по полу:')
    print(comparative_df, '\n')

    '''Контрольный вопрос:
    В данном наборе данных наблюдается кардинальное различие в выживаемости:
    выжили только женщины (100% выживаемость), в то время как все мужчины погибли.
    Средний возраст выживших женщин составляет примерно 29.73 года.
    Из-за того, что в файле нет выживших мужчин и погибших женщин,
    сравнить их средний возраст не представляется возможным.'''

    # --- ФИЛЬТРАЦИЯ ДАННЫХ ---
    print('--- Фильтрация данных ---')

    # Задание 1
    print('Фильтрация. Задание 1')
    mask_t1 = (df['Sex'] == 'male') & (df['Age'] > 30) & (df['Pclass'] == 1)
    task1 = df[mask_t1]
    print(f'Число пассажиров: {len(task1)}')
    print('Первые 10 строк результата:')
    print(task1.head(10), '\n')

    # Задание 2
    print('Фильтрация. Задание 2')
    mask_t2 = ((df['Age'] < 18) | (df['Sex'] == 'female')) & (df['Survived'] == 1)
    task2 = df[mask_t2]
    print(f'Число пассажиров: {len(task2)}\n')

    # Задание 3
    print('Фильтрация. Задание 3')
    mean_fare_3 = df.loc[df['Pclass'] == 3, 'Fare'].mean()
    mask_t3 = (df['Pclass'] == 3) & (df['Fare'] > mean_fare_3)
    task3 = df[mask_t3]
    print(f'Средняя стоимость билета в 3-м классе: {round(mean_fare_3, 2)}')
    print(f'Число пассажиров: {len(task3)}')
    print('Пассажиры:')
    print(task3.head(), '\n')

    # Задание 4
    print('Фильтрация. Задание 4')
    mask_t4 = df['Age'].between(20, 40) & (df['Embarked'] == 'S')
    task4 = df[mask_t4]
    print(f'Число пассажиров: {len(task4)}')
    print('Пассажиры:')
    print(task4.head(), '\n')

    # --- ГРУППИРОВКА И АГРЕГАЦИЯ ---
    # 37
    print('#37')
    group_and_sex_stats = df.groupby(['Pclass', 'Sex']).agg(
        count=('PassengerId', 'count'),
        mean_age=('Age', 'mean'),
        survival_rate=('Survived', lambda x: round(x.mean() * 100, 2)),
        mean_fare=('Fare', 'mean')
    ).round(2)
    print('Группировка по классу и полу:')
    print(group_and_sex_stats, '\n')

    # 38
    print('#38')
    embarked_stats = df.groupby('Embarked').agg(
        count=('PassengerId', 'count'),
        survival_rate=('Survived', lambda x: round(x.mean() * 100, 2))
    ).round(2)
    print('Группировка по порту посадки:')
    print(embarked_stats, '\n')

    # 39
    print('#39')
    survival_by_class = df.groupby('Pclass')['Survived'].mean()
    print('Доля выживших по классам:')
    print(survival_by_class.round(4))
    print(f"Класс с наибольшей долей выживших: {survival_by_class.idxmax()}\n")

    # --- СОХРАНЕНИЕ И ПРОВЕРКА ---
    # 40
    print('#40')
    df.to_csv('titanic_processed.csv', index=False)
    print('Обработанный DataFrame сохранён в titanic_processed.csv\n')

    # 41
    print('#41')
    group_and_sex_stats.to_csv('titanic_statistics.csv')
    print('Результаты группировки по классу и полу сохранены в titanic_statistics.csv\n')

    # 42
    print('#42')
    check = pd.read_csv('titanic_processed.csv')
    print(f'Размер загруженного файла: {check.shape}')
    print(f'Совпадает с обработанным: {check.shape == df.shape}\n')

    '''Выводы по работе:
    #43. Наибольшее количество пропусков содержал признак Cabin (327 пропусков, 78.23% от всех данных).
    На втором месте по количеству пропусков находился признак Age (86 пропусков, 20.57% от всех данных).
    #44. В связи с тем, что доля пропусков в Cabin превысила 50%, данный столбец был удален, 
    поэтому количество столбцов уменьшилось с 12 до 11. Количество строк осталось прежним (418), 
    так как в используемом файле не было пропусков в Embarked. Заполнение пропусков в Age медианой (27 лет) 
    увеличило количество известных значений с 332 до 418. При этом медиана (27), минимум (0) и максимум (76) 
    не изменились. Среднее значение визуально осталось на уровне 30 (из-за округления), а стандартное 
    отклонение уменьшилось с 14 до 13, так как новые значения сгруппировались вокруг медианы.
    #45. В данном наборе данных выживаемость различалась кардинально: выжили 100% женщин и 0% мужчин.
    Общая доля выживших составила 36.36%. Из-за такой специфики выборки средний возраст погибших (29.52) 
    совпал со средним возрастом всех мужчин, а средний возраст выживших (29.73) - со средним возрастом всех женщин.
    #46. Наибольшая доля выживших наблюдалась в 1-м классе (46.73%). Во 2-м и 3-м классах выживаемость 
    была значительно ниже и составила 32.26% и 33.03% соответственно.
    #47. В Pandas наиболее полезными оказались функции загрузки данных (read_csv), исследования структуры 
    (shape, columns, dtypes), обработки пропусков (isna, fillna, dropna), а также инструмент группировки 
    и агрегации данных (groupby и agg). В NumPy крайне полезными оказались методы преобразования столбцов 
    в массивы (to_numpy) и векторные вычисления с использованием логических масок (например, для быстрого 
    расчета средних значений возраста и процентов выживаемости отдельно для мужчин и женщин без использования циклов).'''


if __name__ == "__main__":
    main()