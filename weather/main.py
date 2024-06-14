# # # D:/PROJECTS/100 days python/Day 25/weather_data.csv
# # with open("D:/PROJECTS/100 days python/Day 25/weather_data.csv") as file:
# #        content = file.readlines()
# #        for line in content:
# #               line = line.strip()
# #               print(line)

# # import csv
# #
# # with open("weather_data.csv") as data:
# #        data_file = csv.reader(data)
# #        temp = []
# #        for row in data_file:
# #               temp.append(row[1])
# #        temp.pop(0)
# #        print(temp)
 

# import pandas as pd
# # data = pd.read_csv('D:/PROJECTS/100 days python/Day 25/weather_data.csv')

# # print(data['temp'])

# # data_list = data['temp'].to_list()
# # print(data_list)
# # avg = sum(data_list) / len(data_list)
# # print(avg)
# # print(data)
# # datalist = data["temp"].mean()
# # datalist = data["temp"].sum()
# # datalist = data["condition"]
# # datalist = data[data.temp ==data.temp.max()]
# # datalist = data[data.day == "Monday"]
# # print(datalist)

# disc = {
#     "stduents_name" : ["kali", "raj", "king"],
#     "Score" : [70, 80, 100]
# }

# excel = pd.DataFrame(disc)
# print(excel)

# excel.to_csv("D:/PROJECTS/100 days python/Day 25/new_data.csv")

import pandas as pd

data = pd.read_csv("D:/PROJECTS/100 days python/Day 25/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# colors = []
# for color in data["Primary Fur Color"]:
#      if color not in colors:
#         colors.append(color)
# print(colors)

gray_count = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_count = len(data[data["Primary Fur Color"]== "Black"])

final_part = {"Fur Color" : ["Gray", "Cinnamon", "Black"], "Counts" : [gray_count, cinnamon_count, black_count]}

datas = pd.DataFrame(final_part)
datas.to_csv("D:/PROJECTS/100 days python/Day 25/data.csv")
print(datas)