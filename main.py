# To run and test the code you need to update 4 places:
# 1. Change MY_EMAIL/MY_PASSWORD to your own details.
# 2. Go to your email provider and make it allow less secure apps.
# 3. Update the SMTP ADDRESS to match your email provider.
# 4. Update birthdays.csv to contain today's month and day.
# See the solution video in the 100 Days of Python Course for explainations.


import datetime as dt
import random
import smtplib
import os

# import os and use it to get the Github repository secrets
MY_EMAIL = os.environ.get("MY_EMAIL")
MY_PASSWORD = os.environ.get("MY_PASSWORD")
MY_TARGET = os.environ.get("MY_TARGET")
now = dt.datetime.now
day_of_week = now.weekday()

with open("quotes.txt") as file:
    quotes = file.readlines()

if day_of_week == 0:
    message = random.choice(quotes)
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(user=MY_EMAIL, password=MY_PASSWORD)
    connection.sendmail(
        from_addr=MY_EMAIL,
        to_addrs="MY_TARGET",
        msg="Subject:It's Monday!\n\n"
                f"{message}")

    connection.close()

