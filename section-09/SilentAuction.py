print("""
        _____________
        \\         /
         )_______(
         |"""""""|_.-._,.---------.,_.-._
         |       | | |               | | ''-.
         |       |_| |_             _| |_..-'
         |_______| '-' `'---------'` '-'
         )"""""""(
        /_________\\\\
        `'-------'`
        .-------------.
    ___________________


""")

print("*****Welcome to the Secret Auction Program*****")

bidder={}
go_for_bid=True
while go_for_bid:
    name=str(input("What is your name?: "))
    bid=int(input("What's your bid?: $"))
    bidder[name]=bid #save the data in dictionary

    other_bidder=input("Are there any other bidders? Type 'Yes' or 'No' \n").lower()
    if other_bidder=="no":
        go_for_bid=False
        print("\n"* 100)
        
    elif other_bidder=="yes":
        go_for_bid=True
        print("\n"* 100)
    
    else:
        print("Incorrect Input")

highest_bidder=max(bidder, key=bidder.get)
highest_bid=bidder[highest_bidder]
print(f"The Highest Bid is from {highest_bidder} with a bid of {highest_bid}. ")