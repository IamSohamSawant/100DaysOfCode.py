def is_leap_year(year):
    # Write your code here. 
    # Don't change the function name.
    if year%4==0:
        if year%100==0:
            if year%400==0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
    
year_input=int(input("Enter a year: "))
print(is_leap_year(year_input))