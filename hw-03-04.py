from datetime import datetime, timedelta

def get_congratulation_date(birthday_date):
    weekday = birthday_date.weekday()

    if weekday == 5:
        return birthday_date + timedelta(days=2)
    elif weekday == 6:
        return birthday_date + timedelta(days=1)
    else:
        return birthday_date


def get_upcoming_birthdays(users):
    today = datetime.today().date()
    end_date = today + timedelta(days=7)
    upcoming_birthdays = []

    for user in users:
        birthday_str = user["birthday"]
        birthday_date = datetime.strptime(birthday_str, "%Y.%m.%d").date()

        birthday_this_year = birthday_date.replace(year=today.year)

        if birthday_this_year < today:
            birthday_this_year = birthday_date.replace(year=today.year + 1)

        if today <= birthday_this_year <= end_date:
            congratulation_date = get_congratulation_date(birthday_this_year)

            upcoming_birthdays.append({
                "name": user["name"],
                "congratulation_date": congratulation_date.strftime("%Y.%m.%d")
            })

    return upcoming_birthdays

