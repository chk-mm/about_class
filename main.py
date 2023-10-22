from coffee_maker import CoffeeMaker
from menu import Menu
from money_machine import MoneyMachine

menu = Menu()
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
is_on = True

while is_on:
    choice = input('What would you like? (espresso/latte/flat white): ') or 'latte'

    if choice == 'report':
        coffee_maker.report()  # show the current resource of coffee maker
    elif choice == 'off':
        print('Turn off the coffee maker.')
        is_on = False
    else:
        drink = menu.find_drink(choice)  # check drink in the menu
        if coffee_maker.is_resource_sufficient(drink):  # check resources sufficient
            if money_machine.make_payment(drink.cost):  # insert coins
                coffee_maker.report()
                money_machine.report()
                coffee_maker.make_coffee(drink)  # make coffee