"""An interactive random demo auction.
Run this on the console and place your own bids.
"""
from auction import Auction


def demo_auction():
    """Run a random auction.  Stop after max_bids bidsa"""
    import random
    # number of bids to accept
    max_bids = 13
    bidders = ["Prayut", "Taksin", "Trump", "Obama"]
    auction = Auction("Vacation to Ko Samui", 50)
    print(">>> auction =", auction.__repr__())
    print(">>> auction.start()")
    auction.start()
    pause("Press ENTER to start bidding...")
    nextbidder = 0
    amount = 0
    for n in range(0,max_bids):
        if n % 4 == 3:
            bidder = "You"
            bid = input("Your turn.  How much do you bid? ")
            try:
                amount = float(bid)
                if amount == int(amount): amount = int(amount)
            except:
                amount = auction.best_bid() + 1
                print(f"{bid} is not a valid number. You bid {amount}.")
        else:
            # random bidder
            bestbidder = auction.winner()
            try:
                lastbidder = bidders.index(bestbidder)
            except ValueError:
                lastbidder = 0
            nextbidder = (lastbidder + random.randint(1,len(bidders)-1)) % len(bidders)
            bidder = bidders[nextbidder]
            amount = int(amount - amount%10 + 20*random.randint(1,5)) 
            # ensure first bid is always valid
            if n == 0: amount = max(amount, auction.increment + 10)
        print_and_bid(auction, bidder, amount)

    print()
    print("The bidding has ENDED.")
    pause("Who won?  Press ENTER to see who won... ")
    print()
    print(">>> auction.winner()")
    print(auction.winner())
    print(">>> auction.best_bid()")
    print(auction.best_bid())


def print_and_bid(auction, bidder, amount):
    print(f'>>> bid( "{bidder}", {amount})')
    # wait for ENTER
    #pause()
    try:
        auction.bid(bidder, amount)
    except Exception as e:
        ex_name = type(e).__name__
        print(f'{ex_name}:', e)


def pause(prompt=""):
    """Wait for user to press ENTER."""
    reply = input(prompt)
    return


if __name__ == "__main__":
    demo_auction()
