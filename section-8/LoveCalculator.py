def calculate_love_score():
    print("***RECOMMENDED TO ENTER FULL NAME***")
    name1=input("Enter your Name: ")
    name2=input("Enter the name of the person you Love: ")
    combined_name=(name1+name2)
    lower_name=combined_name.lower()

    t=lower_name.count("t")
    r=lower_name.count("r")
    u=lower_name.count("u")
    e=lower_name.count("e")
    first_name=t+r+u+e

    l=lower_name.count("l")
    o=lower_name.count("o")
    v=lower_name.count("v")
    e=lower_name.count("e")
    second_name=l+o+v+e

    final_name=int(str(first_name)+str(second_name))
    print(final_name)
calculate_love_score()