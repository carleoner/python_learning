class Employee:
    pass

class emp:
    empName = "Peter"
    empAge = 25
    empDesignation = "Manager"

obj = emp()
print(obj.empAge)

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

emp1 = dynamic_emp("Eva", 35, "Dev")
print("Name of the 1st emp: ", emp1.empName)
print("Total emps: ", dynamic_emp.totalEmp)

print("Details: ", emp1.getEmpDetails())
emp1.updateDesignation("DevOp")
print("Details: ", emp1.getEmpDetails())