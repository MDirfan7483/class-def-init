class Employee:
    language = "py"
    salary = 12000
    def __init__(self, name , salary, language):
        self.name = name
        self.salary = salary
        self.language= language
        print("I am creating an object")
    
    
    def getinfo(self):
            print(f"The languge is {self.language}. the salary is {self.salary}")
    

    def Greet(self):
        print("Good mornig")
irfan = Employee("MD.IRFAN", 13000, "Rust")
print( irfan.name, irfan.salary, irfan.language) 

