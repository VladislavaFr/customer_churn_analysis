import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def plot_city_distribution(df: pd.DataFrame) -> None:
    plt.figure(figsize=(8, 5))
    sns.countplot(data=df, x='city')
    plt.title('Распределение клиентов по городам')
    plt.xlabel('Город')
    plt.ylabel('Количество клиентов')
    plt.show()


def plot_churn_distribution(df: pd.DataFrame) -> None:
    plt.figure(figsize=(6, 4))
    sns.countplot(data=df, x='churn')
    plt.title('Распределение churn (оттока)')
    plt.xlabel('Отток (churn)')
    plt.ylabel('Количество клиентов')
    plt.show()
