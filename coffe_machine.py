MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
earning = 0

def compare(drink):
  for item in drink:
    if drink[item] >= resources[item]:
      print(f"sorry we have not enough {item}")
      return False
  return True
  
def money():
  quater = int(input("enter how many quaters ? "))
  dime = int(input("enter how many dimes ? "))
  nickle = int(input("enter how many nickles ? "))
  penny = int(input("enter how many pennies ? "))
  total = quater*0.25 + dime*0.1 + nickle*0.05 + penny*0.01
  return total

def transection(usermoney, costmoney):
  if usermoney >= costmoney:
    global earning
    earning += costmoney
    change = round(usermoney - costmoney , 2)
    print(f"here is your change :{change}$")
    return True
  else:
    print("SORRY NOT ENOUGH MONEY")
    return False

def coffe(orderingredients , resources):
  for item in orderingredients:
    resources[item] -= orderingredients[item]
  print("HERE IS YOUR COFFE!")

ison = True
while ison:
  flavour = input(" what you would like (espresso/latte/cappuccino)")

  if flavour == 'off':
    ison = False
  elif flavour == 'report':
    print(resources)
    print("Money : ",earning)
  else:
    drink = MENU[flavour]
    if compare(drink["ingredients"]):
      totalmoney = money()
      if transection(totalmoney,drink['cost']):
        coffe(drink['ingredients'], resources)