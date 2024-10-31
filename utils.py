from datetime import date, timedelta

def get_all_dates_in_year(year):
    # Start from January 1st of the given year
    current_date = date(year, 1, 1)

    # Define the end date as January 1st of the next year
    end_date = date(year + 1, 1, 1)
    dates = []

    # Loop until we reach the end date
    while current_date < end_date:
        dates.append(current_date.strftime('%Y-%m-%d'))
        current_date += timedelta(days=1)

    return dates
