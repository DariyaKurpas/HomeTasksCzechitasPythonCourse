import math
# employee1 = ["Darinka", "unemployed", 27]
# employee2 = ["Filip", "software engineer", 33]

# def holiday_request(days):
#     if days > employee1["holiday_entitlement"]:
#         employee1["holiday_entitlement"] = employee1["holiday_entitlement"] - days
#         print("Dovolená schválena.")
#     else:
#         print("Na tolik dní už nemáš nárok.")


class Employee:
    def __init__(self, name, position, holidayEntitlement, grossSalary, probationPeriod=False):
        self.name = name
        self.position = position
        self._holidayEntitlement = holidayEntitlement
        self.probationPeriod = probationPeriod
        self.grossSalary = grossSalary
    
    def __str__(self):
        probationPeriodInfo = " and is in probation period" if self.probationPeriod else "."
        return f"The employee {self.name} has a holiday entitlement of {self._holidayEntitlement} days{probationPeriodInfo}. The brutto salary is {self.grossSalary} CZK and their net salary is {math.ceil(self.netSalary)}"

        

    
    def getInfo(self):
        return f"The employee {self.name} has a holiday entitlement of {self._holidayEntitlement} days."
    
    def takeHoliday(self, daysToBeGranted):
        firstName = self.name.split(" ")[0]
        if daysToBeGranted <= self._holidayEntitlement:
            return f"Enjoy the vacation, {firstName}!"
        else:
            return f"Unfortunately, {firstName}, you have only {self._holidayEntitlement} days left in your vacation entitlement. You would like to take {daysToBeGranted - self.holidayEntitlement} more days. Sorry!"
    @property
    def netSalary(self):
        return self.grossSalary * (1-0.15)
    
    @property
    def _lengthOFName(self):
        return len(self.name)
    
    @property
    def _business_card(self):
        if self._lengthOFName < 11:
            return f"{self.name}"
        else:
            firstName = self.name.split(" ")[0][0]
            lastName = self.name.split(" ")[1]
            return f"{firstName}. {lastName}"

    
snouma = Employee("Snouma Minx", "lenoch", 3, 40000, False)
# print(snouma.getInfo())

timmy = Employee("Timmy Minx", "bambula", 2, 35000, True)
# print(timmy.getInfo())

# print(snouma.takeHoliday(1))
# print(timmy.takeHoliday(10))

print(timmy)
print(snouma)
print(snouma._business_card)
print(timmy._business_card)