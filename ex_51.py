#classes

class Employee:
    def __init__(self,fname,lname,pay):
        self.fname=fname
        self.lname=lname
        self.pay=pay
        self.mail=fname+"."+lname+"@company.com"
    def name(self):
        return self.fname+" "+self.lname

emp1=Employee("j","P",3000)
emp2=Employee("M","S",5000)



print(emp1.mail)

print(emp1.name())

##############################################################

class Employee:

    raise_amount=1.08
    no_of_emp=0
    def __init__(self,fname,lname,pay):
        self.fname=fname
        self.lname=lname
        self.pay=pay
        self.mail=fname+"."+lname+"@company.com"
        Employee.no_of_emp+=1

    def apply_raise(self):
        return (self.pay*self.raise_amount)
    
    @classmethod
    def set_raise(cls,amnt):
        cls.raise_amount=amnt

    @classmethod
    def from_string(cls,s):
        fname,lname,pay=s.split("-")
        return cls(fname,lname,pay)

    @staticmethod
    def is_weekday(day):
        if day.weekday()==5 or day.weekday()==6:
            return True
        return False

emp1=Employee("j","P",3000)
emp2=Employee("M","S",5000)

print(emp1.apply_raise())

emp1.set_raise(1.11)

print(emp1.apply_raise())

emp3='j-P-4000'
emp4='M-S-5000'

emp3=Employee.from_string(emp3)

print(emp3.lname)

import datetime

my_date=datetime.date(2020,9,27)

print(Employee.is_weekday(my_date))
