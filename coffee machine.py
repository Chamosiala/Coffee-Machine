water = 400
milk = 540
beans = 120
disposable_cups = 9
money = 550


def show_supply():
    global water, milk, beans, disposable_cups, money
    print("The coffee machine has:")
    print(water, " of water")
    print(milk, " of milk")
    print(beans, " of coffee beans")
    print(disposable_cups, " of disposable cups")
    print("$", money, " of money")


def buy():
    global water, milk, beans, disposable_cups, money
    coffee_type = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
    if coffee_type == '1':
        if water < 250:
            print("Sorry, not enough water!")
            return
        elif beans < 16:
            print("Sorry, not enough beans!")
            return
        water -= 250
        beans -= 16
        money += 4
        print("I have enough resources, making you a coffee!")
    elif coffee_type == '2':
        if water < 350:
            print("Sorry, not enough water!")
            return
        elif milk < 75:
            print("Sorry, not enough milk!")
            return
        elif beans < 20:
            print("Sorry, not enough beans!")
            return
        water -= 350
        milk -= 75
        beans -= 20
        money += 7
        print("I have enough resources, making you a coffee!")
    elif coffee_type == '3':
        if water < 200:
            print("Sorry, not enough water!")
            return
        elif milk < 100:
            print("Sorry, not enough milk!")
            return
        elif beans < 12:
            print("Sorry, not enough beans!")
            return
        water -= 200
        milk -= 100
        beans -= 12
        money += 6
    elif coffee_type == 'back':
        return
    disposable_cups -= 1


def fill():
    global water, milk, beans, disposable_cups, money
    added_water = int(input("Write how many ml of water do you want to add:"))
    water += added_water
    added_milk = int(input("Write how many ml of milk do you want to add:"))
    milk += added_milk
    added_beans = int(input("Write how many grams of coffee beans do you want to add:"))
    beans += added_beans
    added_cups = int(input("Write how many disposable cups of coffee do you want to add:"))
    disposable_cups += added_cups


def take():
    global money
    print("I gave you $", money)
    money = 0


while 1:
    action = input("Write action (buy, fill, take, remaining, exit):")
    if action == "buy":
        buy()
    elif action == "fill":
        fill()
    elif action == "take":
        take()
    elif action == "remaining":
        show_supply()
    elif action == "exit":
        break
