import datetime as dt
import random
import smtplib
now = dt.datetime.now()
weekday = now.weekday() 
# print(weekday)
day = now.day
if weekday == 2:
    with open("100 days python/Birthday Wisher (Day 32) start/quotes.txt") as data:
        all_quotes = data.readlines()
        quote = random.choice(all_quotes)

    # print(quote)
    # Type mail id and app password below
    username = ""
    password = ""
    to_address = "" # To address mail id 

    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(user=username, password=password)
    connection.sendmail(from_addr=username, to_addrs=to_address, msg=f"Subject : Wishes \n\n\n  {quote}")
    connection.close()