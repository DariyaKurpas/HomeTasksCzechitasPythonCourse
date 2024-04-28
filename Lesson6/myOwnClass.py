class Family:
    def __init__(self, name, role, salary, kississsss = 200):
        self._name = name
        self.role = role
        self.salary = salary
        self.kississsss = kississsss
    
    def __str__(self):
        return f"{self._name} is working in this family as {self.role} and gets a salary of {self.salary} per week."
    
    def grounded(self):
        return f"{self._name} is sooooo grounded for today."
    
    @property
    def netSalary(self):
        return f"{self.salary} - 20% back to the government"
    
    def kissing(self):
        return f"{self._name} totally gets at least {self.kississsss}!"
    
snouma = Family("Snouma Minx", "Bunny", "10 loving hugs")
print(snouma.netSalary)
print(snouma)
print(snouma._name)
print(snouma.kissing())