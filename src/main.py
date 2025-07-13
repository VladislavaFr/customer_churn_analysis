from data import load_from_csv, replace_cities
from analysis import basic_analysis
from visualization import plot_city_distribution, plot_churn_distribution

if __name__ == '__main__':
    df = load_from_csv()
    df = replace_cities(df)

    basic_analysis(df)

    plot_city_distribution(df)
    plot_churn_distribution(df)
