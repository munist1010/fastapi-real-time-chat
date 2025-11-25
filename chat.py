from abc import ABC, abstractmethod

class AbstractEmployee(ABC):
    company_name = "Pluralsight"

    def __init__(self, name, employee_id, email):
        self.name = name
        self.employee_id = employee_id
        self.email = email

    def get_contact_info(self):
        return f"{self.name} ({self.company_name}) can be reached at {self.email}"

class Employee:
    company_name = "Pluralsight"

    def __init__(self, name, employee_id, email):
        self.name = name
        self.employee_id = employee_id
        self.email = email

    def get_contact_info(self):
        return f"{self.name} ({self.company_name}) can be reached at {self.email}"

class FullTimeEmployee(Employee):
    def __init__(self, name, employee_id, email, salary):
        super().__init__(name, employee_id, email)
        self.salary = salary
    
    def is_high_earner(self):
        return self.salary >= 100000
        
class Intern(Employee):
    def __init__(self, name, employee_id, email, school):
        super().__init__(name, employee_id, email)
        self.school = school

    def get_contact_info(self):
        return f"{self.name} (from {self.school} at {self.company_name}) can be reached at {self.email}"
