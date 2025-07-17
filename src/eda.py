import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def plot_correlation_heatmap(df: pd.DataFrame) -> None:
    plt.figure(figsize=(10, 8))
    corr = df.corr(numeric_only=True)
    sns.heatmap(corr, annot=True, fmt=".2f", cmap="coolwarm")
    plt.title("Корреляционная матрица признаков")
    plt.show()


def plot_distributions(df: pd.DataFrame) -> None:
    numeric_cols = df.select_dtypes(include='number').columns
    df[numeric_cols].hist(bins=20, figsize=(15, 10), color="skyblue")
    plt.suptitle("Распределения числовых признаков", fontsize=16)
    plt.tight_layout()
    plt.show()


def plot_boxplots_by_churn(df: pd.DataFrame) -> None:
    numeric_cols = df.select_dtypes(include='number').columns
    for col in numeric_cols:
        if col != 'churn':
            plt.figure(figsize=(6, 4))
            sns.boxplot(x='churn', y=col, data=df)
            plt.title(f"{col} в зависимости от churn")
            plt.show()
