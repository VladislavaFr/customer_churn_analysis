import pandas as pd


def basic_analysis(df: pd.DataFrame) -> None:
    print("Первые 5 строк данных:")
    print(df.head())

    print("\nСтатистика по числовым признакам:")
    print(df.describe())

    print("\nРаспределение клиентов по городам:")
    print(df['city'].value_counts())

    print("\nРаспределение churn (оттока):")
    print(df['churn'].value_counts())
