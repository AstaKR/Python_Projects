students = input("Enter the Students heights : ").split()
for n in range (0, len(students)):
    students[n] = int(students[n])

students_count = len(students)
Total_value = 0
for no in range ( 0, students_count ):
    height_value = int(students[no])
    Total_value = Total_value + height_value
average =int(Total_value / students_count)
print(f"Total Heights of students is  {Total_value}")
print(f"Number of Students: {students_count}")
print(f"Students average Heights is {average} ")
    



