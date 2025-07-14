import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def plot_city_distribution(df: pd.DataFrame) -> None:
    plt.figure(figsize=(8, 5))
    sns.countplot(data=df, x='city', color='skyblue')
    plt.title('Распределение клиентов по городам')
    plt.xlabel('Город')
    plt.ylabel('Количество клиентов')
    plt.show()


def plot_churn_distribution(df: pd.DataFrame) -> None:
    plt.figure(figsize=(6, 4))
    sns.countplot(data=df, x='churn', color='salmon')
    plt.title('Распределение churn (оттока)')
    plt.xlabel('Отток (churn)')
    plt.ylabel('Количество клиентов')
    plt.show()


def main():
    # Указываем путь к CSV относительно корня проекта
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    csv_path = os.path.join(base_dir, 'data', 'processed', 'clients_churn.csv')

    print(f"Читаем данные из: {csv_path}")
    df = pd.read_csv(csv_path)

    print(df.info())

    # 1. Распределение клиентов по городам
    plt.figure(figsize=(8, 5))
    sns.countplot(data=df, x='city', color='skyblue')
    plt.title('Количество клиентов по городам')
    plt.xlabel('Город')
    plt.ylabel('Количество')
    plt.show()

    # 2. Распределение оттока (churn)
    plt.figure(figsize=(6, 4))
    sns.countplot(data=df, x='churn', color='salmon')
    plt.title('Распределение оттока клиентов')
    plt.xlabel('Отток (0 - остались, 1 - ушли)')
    plt.ylabel('Количество')
    plt.show()

    # 3. Средний score по оттоку
    plt.figure(figsize=(8, 5))
    sns.barplot(data=df, x='churn', y='score', color='steelblue')
    plt.title('Средний score в зависимости от оттока')
    plt.xlabel('Отток')
    plt.ylabel('Средний score')
    plt.show()

    # 4. Взаимосвязь estimated_salary и loyalty с оттоком
    plt.figure(figsize=(12, 5))

    plt.subplot(1, 2, 1)
    sns.boxplot(data=df, x='churn', y='estimated_salary', color='lightgreen')
    plt.title('Зарплата vs Отток')

    plt.subplot(1, 2, 2)
    sns.boxplot(data=df, x='churn', y='loyalty', color='lightcoral')
    plt.title('Лояльность vs Отток')

    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    main()
