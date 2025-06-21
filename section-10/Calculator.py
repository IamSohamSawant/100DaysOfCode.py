print("""
 _____________________
|  _________________  |
| |Somi           0.| |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|
""")
def add(num1,num2):
    return num1+num2
def subtract(num1,num2):
    return num1-num2
def multiply(num1,num2):
    return num1*num2
def divide(num1,num2):
    return num1/num2

operations={
    "+" :add,
    "-" :subtract,
    "*" :multiply,
    "/" :divide
}

def calculator():
    should_continue=True
    num1=float(input("What is the first number?: "))
    
    while should_continue:
        for symbols in operations:
            print(symbols)
        function_operation=input("Pick a Operator: ")
        num2=float(input("What is the next number?: "))
        function_calculation=operations[function_operation]
        result=function_calculation(num1,num2)
        print(f"{num1} {function_operation} {num2}={result}")
        choice=input("Type 'Y' if you want to continue the operation or Type 'N' for new Calculator. \n").lower()
        if choice=='y':
            num1=result
        else:
            should_continue=False
            print("\n"*20)
            calculator()

calculator()