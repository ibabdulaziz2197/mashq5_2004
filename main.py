10
class Teacher:
    def __init__(name, subject,):
        self.name = name
        self.subject  = subject

    def intoduce(self):
        print(f" {self.model} i {self.ram}")


s1 = Teacher("HP 16GB RAM")

s1.intoduce()


# 11-m
class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def check_balance(self):
        if self.balance == 0:
            print("Hisob bo'sh")
        else:
            print("Balans: 1000$")

b1 = BankAccount(0)

b1.check_balance()


# 12-m
class Light:
    def __init__(self, state):
        self.state = state

    def status(self):
        if self.state == True:
            print("Chiroq yoniq")
        elif self.state == False:
            print("Chiroq o'chiq")

l1 = Light(True)

l1.status()


# 13-m
class Door:
    def __init__(self, is_open):
        self.is_open = is_open

    def check(self):
        if self.is_open == True:
            print("Eshik ochiq")
        else:
            print("Eshik yopiq")

d1 = Door(True)

d1.check()

# 14-m
class GamePlayer:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def result(self):
        if self.score >= 50:
            print("You win!")
        else:
            print("You lose!")

g1 = GamePlayer("Bunyod", 100)

g1.result()

# 15-m
class Temperature:
    def __init__(self, degree):
        self.degree = degree

    def check_weather(self):
        if self.degree == 25:
            print("Issiq")
        else:
            print("Sovuq")

t1 = Temperature(25)
