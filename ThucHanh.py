dept_db = {
    101 : 'HRD',
    102 : 'FINANCE',
    103 : 'ACCOUNTS',
    104 : 'SALES',
    105 : 'ENGINEERING',
    106 : 'SUPPORT'
    }
 
employee_db = { 
    1000: dict(name="Alex",   doj='01-10-89',dept=103),
    1001: dict(name="Mary",   doj='01-11-88', dept=101),
    1002: dict(name="John",   doj='01-10-87', dept=104),
    1003: dict(name="David",  doj='01-06-89', dept=105),
    1004: dict(name="Anne",   doj='01-01-86', dept=106),
    1005: dict(name="Samson", doj='01-02-89', dept=101)
    }

# def employeeInfor (employeeID):
#     if employeeID in employee_db:
#         name = employee_db[employeeID]['name']
#         doj = employee_db[employeeID]['doj']
#         dept = dept_db[employee_db[employeeID]['dept']]
#         return print ("Name: {}, doj: {}, dept: {}".format(name, doj, dept))
#     else:
#         return print ("EmployeeID does not exist.")

# employeeID = int (input ("Please, input your employeeID: "))
# employeeInfor (employeeID)

def getEmployeeData (employeeID):
    if employeeID in employee_db:
        return employee_db[employeeID]
    else:
        return print ("employeeID does not exist.")

def getDeptData (deptID):
    if deptID in dept_db:
        return dept_db[deptID]
    else:
        return "deptID does not exist."

def getEmployeeInfor (employeeID):
    employeeData = getEmployeeData (employeeID)
    for key, value in employeeData.items ():
        if key == "dept":
            print (key, ":", getDeptData(value))
        else:
            print (key, ":", value)
    return

ID = int (input ("Please input employeeID: "))
getEmployeeInfor (ID)

