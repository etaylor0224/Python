import smtplib
import pandas as pd
import datetime as dt
import random

##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

df = pd.read_csv("birthdays.csv")
date_month = dt.datetime.now().month
date_day = dt.datetime.now().day
placeholder = "[NAME]"
email = "email@test.com"
password = "notarealpassword"
letter_choice = random.randint(1,3)

for (index, row) in df.iterrows():
    if row.month == date_month and row.day == date_day:
        bday_name = df.name[index]

with open(fr"letter_templates\letter_{letter_choice}.txt") as letter_data:
    letter = letter_data.read()

letter_temp = letter.replace(placeholder, bday_name)

with smtplib.SMTP("smtp.test.com", port=587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="birthday@person.com",
        msg=f"Subject:Happy Birthday\n\n{letter_temp}")
