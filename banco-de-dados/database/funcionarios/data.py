from datetime import date, timedelta

start_date = date(2019, 1, 1)
number_of_days = 1096

data = []
for day in range(number_of_days):
    a_date = (start_date + timedelta(days = day)).isoformat()
    data.append(a_date)