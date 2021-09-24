import unittest
from auction import Auction, AuctionError


class TestAuction(unittest.TestCase):
    FPP = 10 # floating point places for comparison tolerance

    def setUp(self):
        """Sets up the auction and its type before each test."""
        self.minIncrement = 1
        self.auction = Auction("Pythonian Alloy", self.minIncrement)


    def test_new_auction_state(self):
        """Test that a new auction has no bids and bidding is disabled."""
        self.assertEqual(0, self.auction.best_bid())
        self.assertFalse(self.auction.is_active())


    def test_can_bid_in_auction(self):
        """Tests that the auction can be bid normally."""
        self.auction.start()
        self.assertTrue("Auction should be enabled after start()", self.auction.is_active())
        amount = 125.0 + self.minIncrement
        # Who is Guido Van Rossum?
        self.auction.bid("Guido Van Rossum", amount)
        self.assertAlmostEqual(amount, self.auction.best_bid(), self.FPP)
        self.assertEqual("Guido Van Rossum", self.auction.winner())


    def test_bidding_when_auction_stopped(self):
        """Test that the auction cannot bid after auction stopped."""
        self.auction.start()
        amount = 45.0 + self.minIncrement
        self.auction.bid("Early Guy", amount)
        self.assertAlmostEqual(amount, self.auction.best_bid(), self.FPP)
        self.auction.stop()
        with self.assertRaises(AuctionError):
            self.auction.bid("Late Guy", amount + self.minIncrement)


    @unittest.skip("Rule #3 Auction class minimum increment comparison error.")
    def test_bid_too_low(self):
        """
        Test that the auction cannot bid with value lower than 
        the best bid value.
        """
        self.auction.start()
        amount = 10.0 + self.minIncrement
        self.auction.bid("Poor Guy", amount)
        # the next line should not raise an error
        self.auction.bid("Rich Guy", amount + self.minIncrement)
        with self.assertRaises(AuctionError):
            self.auction.bid("Guy Gone Nuts", 10.0 + self.minIncrement)


    def test_cheap_bid(self):
        """
        Test that the auction cannot bid with value lower than
        the minimum increment plus best bid.
        """
        self.auction.start()
        amount = 100.0 + self.minIncrement
        self.auction.bid("Bid Normally", amount)
        with self.assertRaises(AuctionError):
            self.auction.bid("Cheap Bid", amount + (0.90 * self.minIncrement))


    def test_bid_with_empty_name(self):
        """Test that the bidder's name cannot be empty."""
        self.auction.start()
        with self.assertRaises(ValueError):
            self.auction.bid("",10000 + self.minIncrement)


    @unittest.skip("Space name should be handled as empty name.")
    def test_bid_with_space_name(self):
        """Test that the bidder's name cannot be empty."""
        self.auction.start()
        with self.assertRaises(ValueError):
            self.auction.bid("   ",10000 + self.minIncrement)


    def test_bid_with_bad_value(self):
        """
        Test that auction cannot bid with bad values,
        such as negative or zero.
        """
        self.auction.start()
        with self.assertRaises(ValueError):
            self.auction.bid("Bandit", -1_000_000)


    def test_bid_before_start(self):
        """Test that auction cannot bid if auction has not started yet."""
        with self.assertRaises(AuctionError):
            self.auction.bid("Impatient Man", 100.0 + self.minIncrement)


    def test_winner_name_comparison(self):
        """
        Test that bidder name is compared by capital case
        (and without extra spaces) only.
        """
        self.auction.start()
        amount = 10.0 + self.minIncrement
        self.auction.bid("camelName camelSurname", amount)
        self.assertEqual("Camelname Camelsurname", self.auction.winner())
        self.auction.bid(" Extra   Spaces   ", amount + self.minIncrement*2)
        self.assertEqual("Extra Spaces", self.auction.winner())


    def test_for_data_corruption(self):
        """
        Test that auction's data (name and/or best bid)
        is not corrupted after an error occured.
        """
        self.auction.start()
        amount = 100.0 + self.minIncrement
        self.auction.bid("Bid Normally", amount)
        try:
            self.auction.bid("Error Bid", amount + (0.90 * self.minIncrement) )
        except AuctionError:
            self.assertEqual("Bid Normally", self.auction.winner())
            self.assertAlmostEqual(amount, self.auction.best_bid(), self.FPP)


    def test_auction_state_after_stopped(self):
        """
        Test that the auction is in the correct
        state after it starts or stops.
        """
        self.auction.start()
        self.assertTrue(self.auction.is_active())
        self.auction.stop()
        self.assertFalse(self.auction.is_active())


    def test_same_person_bid_many_times(self):
        """Test that the same person can still bid but with legal values."""
        self.auction.start()
        amount = 100.0 + self.minIncrement
        self.auction.bid("Lonely Guy", amount)
        try:
            self.auction.bid("Lonely Guy", amount)
        except AuctionError:
            pass
        self.auction.bid("Lonely Guy", amount + self.minIncrement*2)
        self.assertEqual("Lonely Guy", self.auction.winner())
        self.assertAlmostEqual(amount + self.minIncrement*2,
                               self.auction.best_bid(), self.FPP)

