import random 
letters=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers=['0','1','2','3','4','5','6','7','8','9']
symbols=['!','@','#','$','%','^','&','*','(',')','_','+']
print("Welcome to PyPassword Generator!")
n_letters=int(input("How many letters would you like in your password? "))
n_symbols=int(input("How many symbols would you like? "))
n_numbers=int(input("How many numbers? "))

#easy level
# password=""
# for char in range(1, n_letters+1):
#     random_character=random.choice(letters)
#     password+=random_character
    
# for char in range(1, n_symbols+1):
#     random_character=random.choice(symbols)
#     password+=random_character
    
# for char in range(1, n_numbers+1):
#     random_character=random.choice(numbers)
#     password+=random_character
    
# print(password)

#Hard Level
password_list=[]
for char in range(1, n_letters+1):
    password_list.append(random.choice(letters))
    
for char in range(1, n_symbols+1):
   password_list.append(random.choice(symbols))
   
for char in range(1, n_numbers+1):
    password_list.append(random.choice(numbers))
   
    
random.shuffle(password_list)


password=""
for char in password_list:
    password+=char
print(password)