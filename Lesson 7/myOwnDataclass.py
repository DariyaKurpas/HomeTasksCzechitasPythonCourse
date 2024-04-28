from dataclasses import dataclass
@dataclass
class Family:
    _name: str
    role: str
    salary: int
    kississsss = 200
    
    def __str__(self):
        return f"{self._name} is working in this family as {self.role} and gets a salary of {self.salary} per week."
    
    def grounded(self):
        return f"{self._name} is sooooo grounded for today."
    
    @property
    def netSalary(self):
        return f"{self.salary} - 20% back to the government"
    
    def kissing(self):
        return f"{self._name} totally gets at least {self.kississsss} kisses!"
    
snouma = Family("Snouma Minx", "Bunny", "10 loving hugs")
print(snouma.netSalary)
print(snouma)
print(snouma._name)
print(snouma.kissing())