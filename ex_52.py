class Employee():
    def __init__(self,fname,lname,pay):
        self.fname=fname
        self.lname=lname
        self.pay=pay
        self.email=fname+"."+lname+"@company.com"
    def fullname(self):
        return self.fname+" "+self.lname



class Developer(Employee):
    def __init__(self,fname,lname,pay,prog_lang):
        super().__init__(fname,lname,pay)  #specify attributes of parent class instead of defining them again
        self.prog_lang=prog_lang


class Manager(Employee):
    def __init__(self,fname,lname,pay,employees=None):
        super().__init__(fname,lname,pay)   
        if employees is None:
            self.employees=[]
        else:
            self.employees=employees  

    def add_emp(self,emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def rem_emp(self,emp):
        if emp in self.employees:
            self.employees.remove(emp)
            
    def print_emp(self):
        for emp in self.employees:
            print(emp.fullname())
            





emp1=Employee("j","p",30000)
print(emp1.email)
print(emp1.fullname())


dev1=Developer("P","J",70000,"python")
print(dev1.fullname())
print(dev1.prog_lang)


dev2=Developer("A","K",76000,"Java")


mgr2=Manager("S","R",90000)

mgr2.add_emp(dev2)

mgr2.print_emp()

###########3

l1=[1,2,3]
l2=[1,2,3]

print(l2== l1)

#############

s = "\t\tWelcome\n"
print(s)
############3

class A:
    def __init__(self, i = 0):
        self.i = i
    
    def print(self):
        print("hello")

class B(A):

    def __init__(self, j = 0):
        super().__init__()
        self.j = j

def main():
    b = B()
    print(b.i)
    print(b.j)

main()



var1=90
def example1():
	
	var1=100
	print("Value of var1:",var1)
var2=55
def example2():
	global var2
	var2=88
	print("Value of var2 inside:",var2)
example1()
example2()
print("Value of var2 outside:",var2)
