import re

class Auction:
    """
    An auction where people can submit bids for an item.
    One Auction instance is for bidding on a single item.

    The rules on an auction are:
    1. a person can submit one or more bids. Each bid must have
       a bid price > 0 and be at least the best bid so far plus 
       a minimum increment (min_increment, default value is 1).
       If a bid is <= 0 then a ValueError is raised.
       If a bid is > 0 but too low then an AuctionError is raised.
    2. See the bid method for required values of parameters.
    3. New bids must exceed the current best bid by a minimum
       increment (min_increment), such as 1 or 0.01.
       The min_increment is specified as a constructor parameter.
    4. The application must call auction.start() to enable bidding,
       and auction.stop() to disable bidding.  
       start() and stop() can be called multiple times. 
       auction.is_active() tests if bidding is enabled.
    5. Bids are allowed only when auction is active.
       If bid() is called when auction is inactive (stopped),
       an AuctionError is thrown.
    6. At any time, best_bid() can be called to get best bid so far,
       and winner() to find the name of top bidder.
 
    Example:
    >>> auction = Auction("TDD with Python, 2nd Edition")
    >>> print("Minimum bid increment is", auction.increment)
    Minimum bid increment is 1
    >>> auction.start()
    >>> auction.bid("Jim", 250)
    >>> auction.bid("Harry", 300)
    >>> auction.bid(" biRd ", 400)
    >>> auction.best_bid()
    400
    >>> auction.winner()
    'Bird'
    >>> auction.bid("Jim", 400.1)
    Traceback (most recent call last):
      ...
    auction.AuctionError: Bid is too low
    >>> auction.bid("", 1000)
    Traceback (most recent call last):
      ...
    ValueError: Missing bidder name
    >>> auction.is_active()
    True
    >>> auction.stop()
    >>> auction.bid("Jim", 1000)
    Traceback (most recent call last):
      ...
    auction.AuctionError: Bidding not allowed now
    >>> auction.start()
    >>> auction.bid("mai", 402.50)
    >>> auction.best_bid()
    402.5
    >>> auction.winner()
    'Mai'
    """

    def __init__(self, auction_name, min_increment=1):
        """Create a new auction with given auction name.

           min_increment is the minimum amount that a new bid must
           exceed the current best bid.
        """
        self.name = auction_name
        self.bids = {"no bids": 0}
        self.increment = min_increment
        self.active = False
    
    def start(self):
        """Enable bidding."""
        self.active = True

    def stop(self):
        """Disable bidding."""
        self.active = False

    def is_active(self):
        """Query if bidding is enabled. Returns True if bidding enabled."""
        return self.active
    
    def bid(self, bidder_name, amount):
        """ 
        Submit a bid to this auction.

        bidder_name - name of bidder, a non-empty non-blank string.
               Names are converted to Title Case, and excess space
               inside and surrounding the string is removed.
               " harry   haCkeR " is normalized to "Harry Hacker"
        amount - amount (int or float) of this bid. Must be positive 
               and greater than previous best bid by at least a
               minimum bid increment, as described in class docstring.

        Throws:
            TypeError if bidder_name or amount are incorrect data types.
            ValueError if bidder_name is only whitespace, or amount < 0.
            AuctionError if bidding disabled or amount is too low.
        """
        if not isinstance(bidder_name, str):
            raise TypeError("Bidder name must be a non-empty string")
        if not isinstance(amount, (int,float)):
            raise TypeError('Amount must be a number')
        if not self.active:
            raise AuctionError('Bidding not allowed now')
        if len(bidder_name) < 1:
            raise ValueError("Missing bidder name")
        if amount < 0:
            raise ValueError('Amount is invalid')
        # check if this is best bid so far
        if amount <= self.best_bid() + self.increment:
            raise AuctionError("Bid is too low")
        # fix case of letters and remove whitespace
        bidder_name = Auction.normalize(bidder_name)
        # Accept the bid!
        self.bids[bidder_name] = amount

    def best_bid(self):
        """Return the highest bid so far."""
        return max(self.bids.values())

    def winner(self):
        """Return name of person who placed the highest bid."""
        best = self.best_bid()
        for (bidder,bid) in self.bids.items():
            if bid == best: return bidder

    def __str__(self):
        """Return a string description for this auction."""
        return 'Auction for '+self.name 

    def __repr__(self):
        """String form of command to recreate the object."""
        if self.increment == 1:
            return(f"Auction('{self.name}')")
        else:
            return(f"Auction('{self.name}', min_increment={self.increment})")

    @classmethod
    def normalize(cls, name):
        """
        Convert a name to title case and remove excess whitespace.

        Examples:
        >>> Auction.normalize("KUNG FU  ")
        'Kung Fu'
        >>> Auction.normalize("KUNG-FU  ")
        'Kung-Fu'
        >>> Auction.normalize("   too    MuCh  SpacE")
        'Too Much Space'
        >>> Auction.normalize("noSpacE")
        'Nospace'
        >>> Auction.normalize("    ")
        ''
        """
        namewords = re.split("\\s+",name.strip())
        name = " ".join(namewords)
        return name.title()


class AuctionError(Exception):
    """
    Exception to throw when an invalid Auction action is performed.
    """
    # Superclass provides all the behavior we need, so nothing to add here.
    pass


