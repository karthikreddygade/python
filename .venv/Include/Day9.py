
def max_bid(bidding):
    bidding_amount=0
    winner = ""
    for bidder in bidding_dictonary:
        bidde_amount = bidding_dictonary[bidder]
        if bidding_amount<bidde_amount:
            bidding_amount == bidde_amount
            winner = bidder
        print(f"Heoghest bidder{winner}with heighest bid of {bidding_amount}")


bidding = {}
bidding_go_on = True
while bidding_go_on:
    name = input("What's your name")
    bid = input("What is your bid amount")
    bidding[name] = bid
    print(bidding)
    ask = input("type yes if any other bidders are there else type no").lower()
    if ask == "no":
        bidding_go_on = False
        max_bid(bidding)
    elif ask =="yes":
        print("\n"*20)
