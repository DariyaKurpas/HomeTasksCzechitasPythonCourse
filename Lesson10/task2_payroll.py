hours = []

with open(r"Lesson10\payroll.txt", encoding="utf-8") as file:
    for time in file:
        hours.append(int(time))
    
print(hours)

hourly_base = float(input("What is your hourly wage?:\n"))

with open("monthly_salary.txt", mode="w", encoding="utf-8") as output:
    for monthly_hours in hours:
        print(hourly_base*monthly_hours, file=output)