
class MyCoffee:
    water = 400
    milk = 540
    beans = 120
    dis_cup = 9
    money = 550

    def __init__(self, user):
        self.user = user
        self.es_water = 250
        self.es_beans = 16
        self.es_money = 4

        self.la_water = 350
        self.la_milk = 75
        self.la_beans = 20
        self.la_money = 7

        self.ca_water = 200
        self.ca_milk = 100
        self.ca_beans = 12
        self.ca_money = 6

    def buy(self):
        if self.user == "buy":
            print()
            print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
            cof = input("> ")
            if cof == "1":
                if MyCoffee.water < self.es_water:
                    print("Sorry, not enough water!")
                elif MyCoffee.beans < self.es_beans:
                    print("Sorry, not enough beans!")
                elif MyCoffee.dis_cup < 1:
                    print("Sorry, not enough disposable cups!")
                else:
                    MyCoffee.water = MyCoffee.water - self.es_water
                    MyCoffee.beans = MyCoffee.beans - self.es_beans
                    MyCoffee.dis_cup = MyCoffee.dis_cup - 1
                    MyCoffee.money = MyCoffee.money + self.es_money
                    print("I have enough resources, making you a coffee!")
            elif cof == "2":
                if MyCoffee.water < self.la_water:
                    print("Sorry, not enough water!")
                elif MyCoffee.milk < self.la_milk:
                    print("Sorry, not enough milk!")
                elif MyCoffee.beans < self.la_beans:
                    print("Sorry, not enough beans!")
                elif MyCoffee.dis_cup < 1:
                    print("Sorry, not enough disposable cups!")
                else:
                    MyCoffee.water = MyCoffee.water - self.la_water
                    MyCoffee.milk = MyCoffee.milk - self.la_milk
                    MyCoffee.beans = MyCoffee.beans - self.la_beans
                    MyCoffee.dis_cup = MyCoffee.dis_cup - 1
                    MyCoffee.money = MyCoffee.money + self.la_money
                    print("I have enough resources, making you a coffee!")

            elif cof == "3":
                if MyCoffee.water < self.ca_water:
                    print("Sorry, not enough water!")
                elif MyCoffee.milk < self.ca_milk:
                    print("Sorry, not enough milk!")
                elif MyCoffee.beans < self.ca_beans:
                    print("Sorry, not enough beans!")
                elif MyCoffee.dis_cup < 1:
                    print("Sorry, not enough disposable cups!")
                else:
                    MyCoffee.water = MyCoffee.water - self.ca_water
                    MyCoffee.milk = MyCoffee.milk - self.ca_milk
                    MyCoffee.beans = MyCoffee.beans - self.ca_beans
                    MyCoffee.dis_cup = MyCoffee.dis_cup - 1
                    MyCoffee.money = MyCoffee.money + self.ca_money
                    print("I have enough resources, making you a coffee!")

    def fill(self):
        if self.user == "fill":
            print("Write how many ml of water do you want to add:")
            add_water = int(input("> "))
            print("Write how many ml of milk do you want to add:")
            add_milk = int(input("> "))
            print("Write how many grams of coffee beans do you want to add:")
            add_beans = int(input("> "))
            print("Write how many disposable cups of coffee do you want to add:")
            add_dis = int(input("> "))
            MyCoffee.water = MyCoffee.water + add_water
            MyCoffee.milk = MyCoffee.milk + add_milk
            MyCoffee.beans = MyCoffee.beans + add_beans
            MyCoffee.dis_cup = MyCoffee.dis_cup + add_dis
            MyCoffee.money = MyCoffee.money

    def take(self):
        if self.user == "take":
            print(f"I gave you ${MyCoffee.money}")
            if MyCoffee.money > 0:
                MyCoffee.money = MyCoffee.money - MyCoffee.money

    def remaining(self):
        if self.user == "remaining":
            print()
            print("The coffee machine has:")
            print(f"{MyCoffee.water} of water")
            print(f"{MyCoffee.milk} of milk")
            print(f"{MyCoffee.beans} of coffee beans")
            print(f"{MyCoffee.dis_cup} of disposable cups")
            if MyCoffee.money == 0:
                print(f"{MyCoffee.money} of money")
            else:
                print(f"${MyCoffee.money} of money")


def main_menu():
    global condition
    print()
    print("Write action (buy, fill, take, remaining, exit):")
    user = input("> ")
    if user == "exit":
        condition = False
    main = MyCoffee(user)
    main.buy()
    main.fill()
    main.take()
    main.remaining()


condition = True
while condition:
    main_menu()
