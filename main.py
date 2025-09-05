import pandas as pd
# Импорт необходимых библиотек
import pandas as pd
import numpy as np

# Шаг 1: Создаём DataFrame с оценками 10 учеников по 5 предметам
data = {
    'Имя': [f'Ученик_{i}' for i in range(1, 11)],
    'Математика': [85, 92, 78, 90, 88, 76, 95, 89, 82, 93],
    'Физика': [79, 85, 80, 88, 91, 74, 90, 87, 83, 86],
    'Химия': [88, 76, 85, 90, 82, 79, 84, 80, 87, 91],
    'История': [90, 88, 92, 85, 87, 93, 80, 89, 84, 86],
    'Литература': [92, 94, 89, 91, 90, 87, 93, 95, 88, 90]
}

df = pd.DataFrame(data)

# Шаг 2: Выводим первые несколько строк DataFrame
print("Первые 5 строк DataFrame:")
print(df.head())
print("\n" + "="*50 + "\n")

# Шаг 3: Средняя оценка по каждому предмету
print("Средняя оценка по каждому предмету:")
mean_scores = df.drop('Имя', axis=1).mean()
print(mean_scores)
print("\n" + "="*50 + "\n")

# Шаг 4: Медианная оценка по каждому предмету
print("Медианная оценка по каждому предмету:")
median_scores = df.drop('Имя', axis=1).median()
print(median_scores)
print("\n" + "="*50 + "\n")

# Шаг 5: Q1 и Q3 для оценок по математике
Q1_math = df['Математика'].quantile(0.25)
Q3_math = df['Математика'].quantile(0.75)
IQR_math = Q3_math - Q1_math

print("Оценки по Математике:")
print(f"Q1: {Q1_math}")
print(f"Q3: {Q3_math}")
print(f"IQR (Межквартильный размах): {IQR_math}")
print("\n" + "="*50 + "\n")

# Шаг 6: Стандартное отклонение по каждому предмету
print("Стандартное отклонение по каждому предмету:")
std_scores = df.drop('Имя', axis=1).std()
print(std_scores)