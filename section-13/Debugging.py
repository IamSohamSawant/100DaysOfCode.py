# def my_function():
#     for i in range(1,21):
#         if i == 20:
#             print("You got it.")

# my_function()

# from random import randint
# random_symbol=["","!","@","#","$","%","^"]
# random_num=randint(1, 6)
# print(random_symbol[random_num])

import random
import maths
def mutile(a_list):
    b_list=[]
    new_item=0
    for item in a_list:
        new_item=2*item
        new_item+=random.randint(1, 3)
        new_item=maths.add(new_item, item)
    b_list.append(new_item)
    print(b_list)
mutile([1,3,5,7,9])
