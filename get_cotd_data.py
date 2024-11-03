import os
import random

import pandas as pd

from datetime import date, timedelta


def get_all_dates_in_year(year: int):
    start_date = date(year, 1, 1)

    end_date = date(year + 1, 1, 1)

    dates = []

    while start_date < end_date:
        dates.append(start_date.strftime("%Y-%m-%d"))
        start_date += timedelta(days=1)

    return dates


if __name__ == "__main__":
    start_year = 2024  # Include this year
    end_year = 2035  # Exclude this year

    languages = pd.read_csv("data/language.csv").language.tolist()

    for year in range(start_year, end_year):
        dates = get_all_dates_in_year(year)
        random.Random(year).shuffle(dates)

        if not os.path.exists(f"cotd/{year}"):
            os.makedirs(f"cotd/{year}")

        for language in languages:
            cotd = []

            try:
                champion_data_df = pd.read_csv(f"data/champion/champion_{language}.csv")
                champion_data_df = champion_data_df.fillna("")
            except FileNotFoundError:
                continue

            for i, d in enumerate(dates):
                cotd.append(
                    [d] + champion_data_df.iloc[i % len(champion_data_df)].tolist()
                )

            # Save the champion for the current language
            cotd_df = pd.DataFrame(
                cotd, columns=["date"] + champion_data_df.columns.tolist()
            )

            cotd_df.to_csv(f"cotd/{year}/{language}.csv", index=False)
