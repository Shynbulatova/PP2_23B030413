
# Python date
# Write a Python program to subtract five days from current date.
from datetime import datetime, timedelta

current_date = datetime.now()
five_days_ago = current_date - timedelta(days=5)
formatted_date = five_days_ago.strftime('%Y-%m-%d')

print("Current Date:", current_date.strftime('%Y-%m-%d'))
print("Five Days Ago:", formatted_date)


# Write a Python program to print yesterday, today, tomorrow.
from datetime import datetime, timedelta

today = datetime.now()
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)

formatted_yesterday = yesterday.strftime('%Y-%m-%d')
formatted_today = today.strftime('%Y-%m-%d')
formatted_tomorrow = tomorrow.strftime('%Y-%m-%d')

print("Yesterday:", formatted_yesterday)
print("Today:", formatted_today)
print("Tomorrow:", formatted_tomorrow)


# Write a Python program to drop microseconds from datetime.
from datetime import datetime

current_datetime = datetime.now()
formatted_datetime = current_datetime.replace(microsecond=0)

print("Original Datetime:", current_datetime)
print("Datetime without Microseconds:", formatted_datetime)


# Write a Python program to calculate two date difference in seconds.
from datetime import datetime

date1 = datetime(2022, 1, 1, 0, 0, 0)
date2 = datetime(2022, 1, 2, 0, 0, 0)

difference = date2 - date1
difference_in_seconds = difference.total_seconds()

print("Difference in seconds:", difference_in_seconds)

