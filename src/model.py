from typing import Tuple
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, f1_score, roc_auc_score, confusion_matrix, RocCurveDisplay
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression


def prepare_data(df: pd.DataFrame):
    import numpy as np
    from sklearn.model_selection import train_test_split
    from sklearn.preprocessing import StandardScaler
    from sklearn.impute import SimpleImputer

    cols_to_drop = ['churn', 'customer_id', 'city']
    existing_cols_to_drop = [col for col in cols_to_drop if col in df.columns]
    X = df.drop(columns=existing_cols_to_drop)
    X = X.select_dtypes(include=[np.number])

    y = df['churn']

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    # Заполнение пропусков медианой
    imputer = SimpleImputer(strategy='median')
    X_train_imputed = imputer.fit_transform(X_train)
    X_test_imputed = imputer.transform(X_test)

    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train_imputed)
    X_test_scaled = scaler.transform(X_test_imputed)

    return X_train_scaled, X_test_scaled, y_train, y_test


def train_model(df: pd.DataFrame) -> None:
    X_train, X_test, y_train, y_test = prepare_data(df)

    # Обучаем логистическую регрессию
    model = LogisticRegression(random_state=42)
    model.fit(X_train, y_train)

    # Предсказания на тесте
    y_pred = model.predict(X_test)
    y_pred_proba = model.predict_proba(X_test)[:, 1]

    # Метрики
    acc = accuracy_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)
    roc_auc = roc_auc_score(y_test, y_pred_proba)

    print(f"Accuracy: {acc:.3f}")
    print(f"F1-score: {f1:.3f}")
    print(f"ROC AUC: {roc_auc:.3f}")

    # Матрица ошибок
    cm = confusion_matrix(y_test, y_pred)
    print("Confusion Matrix:")
    print(cm)

    # Визуализация ROC-кривой
    RocCurveDisplay.from_estimator(model, X_test, y_test)
    plt.show()


def train_model(df):
    print("train_model запущена")
    X_train, X_test, y_train, y_test = prepare_data(df)

    print("Обучение модели...")

    model = LogisticRegression(class_weight='balanced', random_state=42, max_iter=1000)
    model.fit(X_train, y_train)

    print("Модель обучена. Делаем предсказания...")

    y_pred = model.predict(X_test)

    accuracy = accuracy_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)

    print(f"Accuracy: {accuracy:.3f}")
    print(f"F1-score: {f1:.3f}")

if __name__ == "__main__":
    import src.data as data

    print("Старт main")  # чтобы убедиться, что блок сработал

    df = data.load_from_csv()
    df = data.replace_cities(df)
    train_model(df)