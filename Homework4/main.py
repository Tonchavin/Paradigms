# Используем библиотеку pandas и ее функцию для подсчета корреляции
import pandas as pd

if __name__ == '__main__':
    df = {
        "Array_1": [1, 2, 5, 7, 8],
        "Array_2": [2, 4, 6, 8, 10]
    }
    data = pd.DataFrame(df)
    print(round(data.corr(), 4))
