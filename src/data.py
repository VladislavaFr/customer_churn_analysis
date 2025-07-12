import os
import sqlite3
import pandas as pd

def load_clients_churn() -> pd.DataFrame:
    # Получаем путь к текущему файлу data.py
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # base_dir — это корень проекта, папка выше, чем папка src

    # Строим путь к базе данных относительно корня проекта
    db_path = os.path.join(base_dir, 'data', 'raw', 'banks.db')

    # Подключаемся к базе
    conn = sqlite3.connect(db_path)

    query = "SELECT * FROM clients_churn"
    clients_churn_df = pd.read_sql_query(query, conn)

    conn.close()
    return clients_churn_df

def save_to_csv(df: pd.DataFrame) -> None:
    """
    Сохраняет DataFrame в CSV файл
    """
    processed_path = os.path.join('data', 'processed')
    os.makedirs(processed_path, exist_ok=True)
    csv_path = os.path.join(processed_path, 'clients_churn.csv')
    df.to_csv(csv_path, index=False)
    print(f"Данные сохранены в {csv_path}")

def load_from_csv() -> pd.DataFrame:
    """
    Загружает данные из CSV в DataFrame
    """
    csv_path = os.path.join('data', 'processed', 'clients_churn.csv')
    df = pd.read_csv(csv_path)
    return df

def replace_cities(df: pd.DataFrame) -> pd.DataFrame:
    """
    Заменяет значения в столбце 'city' согласно словарю city_map
    """
    city_map = {
        'Город_Р': 'Рязань',
        'Город_Я': 'Ярославль',
        'Город_В': 'Владимир'
    }
    df['city'] = df['city'].replace(city_map)
    return df

if __name__ == '__main__':
    df = load_clients_churn()
    save_to_csv(df)
    df = load_from_csv()
    df = replace_cities(df)
    save_to_csv(df)
