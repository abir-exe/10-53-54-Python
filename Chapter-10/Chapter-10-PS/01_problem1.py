class Programmer:
    company = "Microsoft"
    def __init__(self, name, salary, pin):
        self.name = name
        self.salary = salary
        self.pin = pin

p = Programmer("Harry", "13000", "232")
print(p.name, p.salary, p.pin)
r = Programmer("Rohan", "13000", "232")
print(r.name, r.salary, r.pin)