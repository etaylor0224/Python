import smtplib
import datetime as dt
import random

now = dt.datetime.now()
day_num = now.weekday()

with open("quotes.txt") as quotes:
    quote_lst = quotes.readlines()
quote_temp = [quote.strip("\n") for quote in quote_lst]

def email():
    quote = random.choice(quote_temp)
    my_email = ("SANITIZED")
    password = "SANITIZED"

    with smtplib.SMTP("SANITIZED", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="SANITIZED",
            msg=f"Subject:Motivation\n\n{quote}")

if day_num == 4:
   email()
else:
    pass
