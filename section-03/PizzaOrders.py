print("Welcome to the Python Pizza Deliveries!!")
bill=0
size=input("What size of pizza do you want? S, M or L: ")
pepperoni=input("Do you want pepperoni on your pizza? Y or N ")
extra_cheese=input("Do you want extra cheese , Y or N: ")
if size=="S":
    bill+=15
    print("Price of small pizza is $15")
    if pepperoni=="Y":
        bill+=2
        print("Pepperoni for Small pizza price: $2")
    else:
        print("Enjoy eating your pizza")

elif size=="M":
    bill+=20
    print("Price of Medium pizza is $20")
    if pepperoni=="Y":
        bill+=3
        print("Pepperoni for Medium pizza price: $3")
    else:
        print("Enjoy eating your pizza")

elif size=="L":
    bill+=25
    print("Price of Large pizza is $25")
    if pepperoni=="Y":
        bill+=3
        print("pepperoni for Large pizza price: $3")
    else:
        print("Enjoy eating your pizza")
else:
    print("Invalid size entered!")
if size in['S','M','L'] and extra_cheese=="Y":
    bill+=1
    print("Extra cheese added: $1")

print(f"Your final bill is: ${bill}")
#Direct bill pan kadu shakto print lihaychi garaj nai hai.