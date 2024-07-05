hours = []

with open(r"Lesson10\payroll.txt", encoding="utf-8") as file:
    for time in file:
        hours.append(int(time))
    
print(hours)

hourly_base = float(input("What is your hourly wage?:\n"))

whole_salary = 0

for item in hours:
    whole_salary = whole_salary + item * hourly_base

print(f"The whole salary for year 2023 is {whole_salary} EUR.")

average_salary = whole_salary / len(hours)

print(f"The average monthly salary was {average_salary} EUR.")