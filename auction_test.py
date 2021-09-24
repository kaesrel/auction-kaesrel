"""Tests of the Auction class.

Author: your name
"""
import unittest
from auction import Auction, AuctionError


class TestAuction(unittest.TestCase):
    """Tests of the Auction class."""

    def setUp(self):
        """Set up an auction before each test."""
        # you can still create an auction inside a test if you want special values
        self.auction = Auction("test auction")


    def test_new_auction(self):
        """Test that a new auction has no bids and bidding is disabled."""
        self.assertEqual(0, self.auction.best_bid())
        self.assertEqual('no bids', self.auction.winner())
