import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_city_distribution(df: pd.DataFrame) -> None:
    plt.figure(figsize=(8, 5))
    sns.countplot(data=df, x='city', palette='Set2')
    plt.title('Распределение клиентов по городам')
    plt.xlabel('Город')
    plt.ylabel('Количество клиентов')
    plt.show()

def plot_churn_distribution(df: pd.DataFrame) -> None:
    plt.figure(figsize=(6, 4))
    sns.countplot(data=df, x='churn', palette='Set1')
    plt.title('Распределение оттока клиентов (churn)')
    plt.xlabel('Отток (0 - остались, 1 - ушли)')
    plt.ylabel('Количество клиентов')
    plt.show()

def plot_score_by_churn(df: pd.DataFrame) -> None:
    plt.figure(figsize=(8, 5))
    sns.barplot(data=df, x='churn', y='score', palette='coolwarm')
    plt.title('Средний score в зависимости от оттока')
    plt.xlabel('Отток')
    plt.ylabel('Средний score')
    plt.show()

def plot_salary_and_loyalty_by_churn(df: pd.DataFrame) -> None:
    plt.figure(figsize=(12, 5))

    plt.subplot(1, 2, 1)
    sns.boxplot(data=df, x='churn', y='estimated_salary', palette='Pastel1')
    plt.title('Зарплата vs Отток')

    plt.subplot(1, 2, 2)
    sns.boxplot(data=df, x='churn', y='loyalty', palette='Pastel2')
    plt.title('Лояльность vs Отток')

    plt.tight_layout()
    plt.show()

def main():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    csv_path = os.path.join(base_dir, 'data', 'processed', 'clients_churn.csv')

    print(f"Читаем данные из: {csv_path}")
    df = pd.read_csv(csv_path)

    print("Общая информация о данных:")
    print(df.info())

    plot_city_distribution(df)
    plot_churn_distribution(df)
    plot_score_by_churn(df)
    plot_salary_and_loyalty_by_churn(df)

if __name__ == '__main__':
    main()