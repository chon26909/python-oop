class Employee:

    company_name = "HiChon Company"

    minSalary = 10000
    maxSalary = 50000

    def __init__(self,name,salary,department):
        #private
        self.__name = name
        self.__salary = salary
        self.__department = department

        #protect
    def _showData(self):
        print("ชื่อ : {} ".format(self.__name))
        print("เงินเดือน : {} ".format(self.__salary))
        print("แผนก : {} ".format(self.__department))

    def getIncomePerYear(self):
        return self.__salary * 12

    def __str__(self):
        return ("ชื่อ : {} แผนก : {} เงินเดือน : {} รายได้ต่อปี : {}".format(self.__name, self.__department, self.__salary, self.getIncomePerYear()))

    def setName(self, newName): 
        self.__name = newName

    def getName(self): 
        return self.__name

class Accounting(Employee):

    __departmentName = "บัญชี"

    def __init__(self,name,salary,age):
        super().__init__(name, salary, self.__departmentName)
        self.__age = age

    def _showData(self):
        super()._showData()
        print("อายู {}".format(self.__age))

class Programmer(Employee):

    __departmentName = "โปรแกรมเมอร์"

    def __init__(self,name,salary,skill,experience):
        super().__init__(name, salary, self.__departmentName)
        self.__skill = skill
        self.__experience = experience
       
    def _showData(self):
        super()._showData()
        print("ทักษะ {}".format(self.__skill))
        print("ประสบการณ์ {}".format(self.__experience))

class Sale(Employee):

    __departmentName = "ขายสินค้า"

    def __init__(self,name,salary,area):
        super().__init__(name, salary, self.__departmentName)
        self.__area = area

    def _showData(self):
        super()._showData()
        print("พื้นที่ : {} ".format(self.__area))


account = Accounting("chon", 25000, 30)
account._showData()

programmer = Programmer("boss", 35000, "code", 1)
programmer._showData()

sale = Sale("june", 3000, "bangkok")
sale._showData()