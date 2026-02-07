from datetime import datetime

def get_days_from_today(date: str):
    try:
        current_date = datetime.today()
        external_date = datetime.strptime(date, '%Y-%m-%d')

        return current_date.toordinal() - external_date.toordinal()
    except ValueError:
        return 'Invalid date format, please use YYYY-MM-DD format'

