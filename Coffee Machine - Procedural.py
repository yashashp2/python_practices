MENU = {
    "espresso": {
        "ingredients" : {
            "water" : 50,
            "coffee" : 18,
        },
        "cost" : 1.5,
    },

    "latte": {
        "ingredients" : {
            "water" : 200,
            "milk" : 150,
            "coffee" : 24,
        },
        "cost" : 2.5,
    },

    "cappuccino": {
        "ingredients" : {
            "water" : 250,
            "milk" : 100,
            "coffee" : 24,
        },
        "cost" : 3.0,
    }
}

resources = {
    "water" : 500,
    "milk" : 500,
    "coffee" : 500,
}


machine_status = "on" #Once a transaction is completed, the machine starts a new transaction until "machine_status" is "on"
money = 0 #to keep track of amount inserted by a customer
profit = 0 #to keep track of amount in the machine
change = 0 #to keep track of the change to be given after a successfull transaction

def resource_check(user_choice):
    for resource in MENU[user_choice]["ingredients"]:
        if resources[resource] < MENU[user_choice]["ingredients"][resource]: #check if enough resources available to serve the drink
            print("Sorry! Not enough resources. Come back later.")
            return
    money = amount_calculation()
    transaction(money, user_choice) #calls the function to do the transaction

def amount_calculation():
    print("Please insert coins")
    quarters = int(input("How many quarters?: ")) #1 quarters = 0.25
    dimes = int(input("How many dimes?: ")) #1 dimes = 0.10
    nickles = int(input("How many nickles?: ")) #1 nickles = 0.05
    pennies = int(input("How many pennies?: ")) #1 pennies = 0.01

    money = (0.25 * quarters) + (0.10 * dimes) + (0.05 * nickles) + (0.01 * pennies) #calculates the total amount inserted by the customer
    return money

def transaction(money, user_choice):
    global profit
    if money >= MENU[user_choice]["cost"]: #check if user has inserted enough amount
        profit += MENU[user_choice]["cost"] #the cost of the item is added to profit
        print("Profit:", profit)
        change = money - MENU[user_choice]["cost"] #calculate the change to be given
        print(f"Here is ${round(change,2) } in change")

        for resource in MENU[user_choice]["ingredients"]: #Loop to reduce the amount of resources used by the drink
            resources[resource] -= MENU[user_choice]["ingredients"][resource]        
        print(f"Here is your {user_choice}. Please enjoy!")

    else:
        print("Sorry! That's not enough money. Amount refunded: ", round(money, 2)) #if user has not inserted enough money

while machine_status == "on":
    choice = input("What would you like? (espresso - $1.5 /latte - $2.5 /cappuccino - $3.0):")
    if choice == "off":
        machine_status = "off" #terminates the program from execution

    elif choice == "report":
        for resource in resources:
            print(resource, ": ", resources[resource])

    elif choice == "espresso":
        resource_check(choice)

    elif choice == "latte":
        resource_check(choice)

    elif choice == "cappuccino":
        resource_check(choice)
