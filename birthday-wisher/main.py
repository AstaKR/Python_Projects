
import datetime as dt
import pandas
import random
import smtplib

# Type mail id and app password below
username = ""
password = ""

today = dt.datetime.now()
today_tuple = (today.month, today.day)

#
# data = pandas.read_csv("birthdays.csv")
# new_dict = {(data_row["month"], data_row["day"]) : data for (index, data_row) in data.iterrows()}


data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row["month"], data_row["day"]): data for (index, data_row) in data.iterrows()}
if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
# if today_tuple in new_dict:
#     birthday_person = new_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=username, password=password)
        connection.sendmail(from_addr=username, to_addrs=birthday_person["email"],msg=f"Subject:Happy Birthday \n\n {contents}")