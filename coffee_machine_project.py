MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def print_resource():
    print(f" Water : {resources["water"]}ml")
    print(f" MIlk : {resources["milk"]}ml ")
    print(f" Coffee : {resources["coffee"]}g")
    print(f" Money : $ {profit}")

def order_process(res, order):
    new_res = {}
    for i in res:
        new_res[i] = res[i] - order["ingredients"][i]
    return new_res

def insert_coins():
    total = 0
    total = float(input("How many quarters : ")) * 0.25
    total += float(input("How many dimes : ")) * 0.10
    total += float(input("How many nickles : ")) * 0.05
    total += float(input("How many pennies : ")) * 0.01
    return total


def user_change(drink_cost,u_coins):
    global profit
    if u_coins >= drink_cost["cost"]:
        print(f"Lets drink the coffee ")
        profit = drink_cost["cost"]
        print_resource()
        change = round(u_coins - drink_cost["cost"], 2)
        print(f"Kindly collect  ${change} change ")
        
    else:
        print(f"Sorry that's not enough money. Money refunded.")


def is_resources_sufficient(resource_list, orders):
    global resources
    for i in resource_list:
        if orders["ingredients"][i] <= resource_list[i]:
            resources[i] = resource_list[i] - orders["ingredients"][i]
            print(f"{i},  {resources[i]}")
        else:
            resources[i] = resource_list[i] - orders["ingredients"][i]
            print(f"Sorry there is not enough{i}, Machine {i} value is {resources[i]}")
            return False
    return True

is_order_over = False
while not is_order_over:

    order_list = input("What would you like? (espresso/latte/cappuccino):")

    if order_list == "off":
        is_order_over = True
    elif order_list == "report":
        print(f"report after purchasing {order_list}:")
        print_resource()
    drinks = MENU[order_list]
    if is_resources_sufficient(resources, drinks):
        user_amount = insert_coins()
        # print(user_amount)
        user_change(drinks, user_amount)



# OUTPUTS:
# What would you like? (espresso/latte/cappuccino):latte
# water,  100
# milk,  50
# coffee,  76
# How many quarters : 10
# How many dimes : 0
# How many nickles : 0
# How many pennies : 0
# Lets drink the coffee
#  Water : 100ml
#  MIlk : 50ml
#  Coffee : 76g
#  Money : $ 2.5
# Kindly collect  $0.0 change
# What would you like? (espresso/latte/cappuccino):    