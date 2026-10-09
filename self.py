class Employee:
    language = "py"
    salary = 12000
    def Greet(self):
        print("Good mornig")

    def getinfo(self):
        print(f"The languge is {self.language}. the salary is {self.salary}")
irfan = Employee()
irfan.language= "c++"
irfan.name = "Irfan"
# print( irfan.name, irfan.salary, irfan.language) 

irfan.getinfo()
irfan.Greet()     