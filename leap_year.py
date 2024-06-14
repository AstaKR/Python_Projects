year= int(input("Enter the year: "))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"This {year} is leap year.")
        else:
            print(f"This {year} is not leap year.")
    else:
        print(f"This {year} is leap year.")
else:
    print(f"This {year} is not leap year.")

# Output:
# Enter the year: 2024
# This 2024 is leap year.