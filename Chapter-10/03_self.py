class Employe:
    language = "Python"
    salary = 1200000
    
    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

harry = Employe()
harry.language = "JavaScript"
harry.getInfo()
# Employe.getInfo(harry)