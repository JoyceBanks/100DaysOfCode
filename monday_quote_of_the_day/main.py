import smtplib
import datetime as dt
import random

MY_EMAIL = #EMAIL
MY_PASSWORD = #PASSWORD

now = dt.datetime.now()
day_of_week = now.weekday()
# print(day_of_week)
with open("quotes.txt", "r") as file:
    quote = file.readlines()
    random_quote = random.choice(quote)
    if day_of_week == 4:
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs= #DESTINATION ADDRESS,
                msg=f"Subject: Quote of the Day\n\n{random_quote}"
                )
