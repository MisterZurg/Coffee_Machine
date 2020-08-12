class CoffeMachine:
    n_machines = 0

    def __new__(cls, *args, **kwargs):
        cls.n_machines += 1
        return object.__new__(cls)

    def __init__(self):
        self.waterMl = 400
        self.milkMl = 540
        self.coffeeBeansGr = 120
        self.amountOfMoney = 550
        self.disposableCups = 9

    def users_action(self):
        users_action = str(input("Write action (buy, fill, take, remaining, exit):\n"))
        if users_action == "buy":
            users_action = (
                input("What do you want to buy? 1 - espresso, "
                      "2 - latte, "
                      "3 - cappuccino, "
                      "back - to main menu:\n"))
            self.buy_coffee(users_action)
            # inputed_action = ""
        elif users_action == "fill":
            add_list =[0,0,0,0]
            info_list = ["Write how many ml of water do you want to add:",
                         "Write how many ml of milk do you want to add:",
                         "Write how many grams of coffee beans do you want to add:",
                         "Write how many disposable cups of coffee do you want to add"
                         ]
            for i in range(4):
                print(info_list[i])
                add_list[i]=int(input())
            self.fill_resourses(add_list)
        elif users_action == "take":
            self.take_money()
        elif users_action == "remaining":
            self.print_info()
        elif users_action == "exit":
            exit()

    def buy_coffee(self, users_choice):
        if users_choice == "1":  # espresso
            if (self.waterMl < 250):
                print("Sorry, not enough water!\n")
                self.users_action()
            elif (self.coffeeBeansGr < 16):
                print("Sorry, not enough coffee beans!\n")
                self.users_action()
            elif (self.disposableCups == 0):
                print("Sorry, not enough disposable cups!\n")
                self.users_action()
            else:
                self.waterMl -= 250
                self.coffeeBeansGr -= 16
                self.amountOfMoney += 4
                self.disposableCups -= 1
                print("I have enough resources, making you a coffee!\n")
                self.users_action()

        elif users_choice == "2":  # latte
            if (self.waterMl < 350):
                print("Sorry, not enough water!\n")
                self.users_action()
            elif (self.milkMl < 75):
                print("Sorry, not enough milk!\n")
                self.users_action()
            elif (self.coffeeBeansGr < 20):
                print("Sorry, not enough coffee beans!\n")
                self.users_action()
            elif (self.disposableCups == 0):
                print("Sorry, not enough disposable cups!\n")
                self.users_action()
            else:
                self.waterMl -= 350
                self.milkMl -= 75
                self.coffeeBeansGr -= 20
                self.amountOfMoney += 7
                self.disposableCups -= 1
                print("I have enough resources, making you a coffee!\n")
                self.users_action()

        elif users_choice == "3":  # cappuccino
            if (self.waterMl < 200):
                print("Sorry, not enough water!\n")
                self.users_action()
            elif (self.milkMl < 100):
                print("Sorry, not enough milk!\n")
                self.users_action()
            elif (self.coffeeBeansGr < 12):
                print("Sorry, not enough coffee beans!\n")
                self.users_action()
            elif (self.disposableCups == 0):
                print("Sorry, not enough disposable cups!\n")
                self.users_action()
            else:
                self.waterMl -= 200
                self.milkMl -= 100
                self.coffeeBeansGr -= 12
                self.amountOfMoney += 6
                self.disposableCups -= 1
                print("I have enough resources, making you a coffee!\n")
                self.users_action()
        else:
            self.users_action()

    def fill_resourses(self,added):
        self.waterMl+=added[0]
        self.milkMl += added[1]
        self.coffeeBeansGr += added[2]
        self.disposableCups += added[3]
        self.users_action()

    def print_info(self):
        print(f"The coffee machine has:\n"
              f"{self.waterMl} of water\n"
              f"{self.milkMl} of milk\n"
              f"{self.coffeeBeansGr} of coffee beans\n"
              f"{self.disposableCups} of disposable cups\n"
              f"{self.amountOfMoney} of money\n")
        self.users_action()

    def take_money(self):
        print(f"I gave you ${self.amountOfMoney}")
        self.amountOfMoney = 0
        self.users_action()

CoffeAutomat = CoffeMachine()
CoffeAutomat.users_action()