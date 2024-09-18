class Employee:
    def __init__(self,name,designation,salary) -> None:
        self.name = name
        self.designation = designation
        self.salary = salary
    
    def __str__(self) -> str:
        return f"{self.name} is a {self.designation} and earns {self.salary} per month"
 
emp1=Employee("John","Manager",None)
print(emp1)
