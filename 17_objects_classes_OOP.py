class Employee:
    pass

class emp:
    empName = "Peter"
    empAge = 25
    empDesignation = "Manager"
    def name():
        print("emp")

class intern(emp):
    def name():
        print("intern")

obj = emp()

######################################
# Dynamic

class dynamic_emp():
    totalEmp = 0

    def __init__(self, empName, empAge, empDesignation):
        self.empName = empName
        self.empAge = empAge
        self.empDesignation = empDesignation
        
        dynamic_emp.totalEmp += 1
    
    def getEmpDetails (self):
        return self.empName, self.empAge, self.empDesignation
    
    def updateDesignation(self, newDesig):
        self.empDesignation = newDesig
        print("Designation updated")
        return self.empDesignation

class intern (dynamic_emp):
    def __init__(self, empName, empAge, empDesignation, internPeriod):
        self.internPeriod = internPeriod
        dynamic_emp.__init__(self, empName, empAge, empDesignation)
    
    def getPeriod(self):
        return "Intern Period in months: ", self.internPeriod

emp1 = dynamic_emp("Eva", 35, "Dev")
print("Name of the 1st emp: ", emp1.empName)
print("Total emps: ", dynamic_emp.totalEmp)

print("Details: ", emp1.getEmpDetails())
emp1.updateDesignation("DevOp")
print("Details: ", emp1.getEmpDetails())

intern1 = intern("John", 21, "intern", 5)
print("Intern details: ", intern1.getEmpDetails())
print(intern1.getPeriod())

#########################################
# polymorphism

class base:
    def name():
        pass
class derived:
    def name():
        print("EOF")
obj = derived
obj.name()