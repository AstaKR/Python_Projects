import math
def paint_calc(height, width,coverage):
    number_of_cans = float((height  * width) / coverage)
    number_of_cans = math.ceil(number_of_cans)
    print(f"You\'ll need {number_of_cans} cans of paints")

height = int(input("Enter the Height value: "))
width = int(input("Enter the width values: "))
coverage = 5
paint_calc(height=height, coverage=coverage, width=width)