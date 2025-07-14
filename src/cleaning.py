import os
import pandas as pd

def load_data() -> pd.DataFrame:
    csv_path = os.path.join('data', 'processed', 'clients_churn.csv')
    df = pd.read_csv(csv_path)
    print("Данные загружены:")
    print(df.head())
    return df

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    print("\nРазмер до очистки:", df.shape)

    # Удаляем дубликаты
    df = df.drop_duplicates()
    print("Удалили дубликаты. Размер:", df.shape)

    # Проверяем пропуски
    print("\nПропущенные значения:")
    print(df.isnull().sum())

    # Удалим строки с пропусками (если они есть)
    df = df.dropna()
    print("После удаления пропусков:", df.shape)

    # Проверка отрицательных значений зарплаты
    df = df[df['estimated_salary'] >= 0]

    # Проверим типы данных
    print("\nТипы данных:")
    print(df.dtypes)

    return df

def save_clean_data(df: pd.DataFrame) -> None:
    cleaned_path = os.path.join('data', 'processed', 'clients_churn_cleaned.csv')
    df.to_csv(cleaned_path, index=False)
    print(f"\nДанные сохранены в {cleaned_path}")

if __name__ == '__main__':
    df = load_data()
    df_clean = clean_data(df)
    save_clean_data(df_clean)