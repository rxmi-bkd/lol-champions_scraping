import os
import random

import pandas as pd

from utils import get_all_dates_in_year

if __name__ == '__main__':
    start_year = 2024 # Include this year
    end_year = 2035 # Exclude this year

    languages_df = pd.read_csv('languages.csv')
    codes = languages_df.code.tolist()

    for year in range(start_year, end_year):
        dates = get_all_dates_in_year(year)
        random.Random(year).shuffle(dates) # Shuffle the dates for random cotd

        if not os.path.exists(f'cotd_data/{year}'):
            os.makedirs(f'cotd_data/{year}')

        for code in codes:
            cotd_data = []

            try:
                champions_data_df = pd.read_csv(f'champions_data/champions_data_{code}.csv')
                champions_data_df = champions_data_df.fillna('')
            except FileNotFoundError:
                continue

            for i, date in enumerate(dates):
                cotd_data.append([date] + champions_data_df.iloc[i % len(champions_data_df)].tolist())

            # Save the data for the current language
            cotd_data_df = pd.DataFrame(cotd_data, columns=['date'] + champions_data_df.columns.tolist())
            cotd_data_df.to_csv(f'cotd_data/{year}/cotd_data_{code}.csv', index=False)
