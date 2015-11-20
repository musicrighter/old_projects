# Unit tests for Card and Deck classes
#
# John Conery
# CIS 211
# Spring 2014
#

import unittest

from Card import *

class CardTest(unittest.TestCase):

    def test_01_cards(self):
        "make some cards, check values returned by accessor methods"
        h = [Card(i) for i in range(0,52,14)]
        for i in range(len(h)):
            self.assertEqual(i, h[i].rank(), "wrong rank in card " + str(i))
            self.assertEqual(i, h[i].suit(), "wrong suit in card " + str(i))
        
        "check representations"        
        self.assertIn(repr(h[0]), ['2\u2663', '2C'], "expected representation to be 2\u2663 or 2C")
        self.assertIn(repr(h[1]), ['3\u2666', '3D'], "expected representation to be 2\u2666 or 3D")
        self.assertIn(repr(h[2]), ['4\u2665', '4H'], "expected representation to be 2\u2665 or 4H")
        self.assertIn(repr(h[3]), ['5\u2660', '5S'], "expected representation to be 2\u2660 or 5S")

        self.assertIn(repr(Card(8)), ['10\u2663', '10C'], "expected representation to be 10\u2663 or 10C")
        self.assertIn(repr(Card(9)), ['J\u2663', 'JC'], "expected representation to be J\u2663 or JC")
        self.assertIn(repr(Card(10)), ['Q\u2663', 'QC'], "expected representation to be Q\u2663 or QC")
        self.assertIn(repr(Card(11)), ['K\u2663', 'KC'], "expected representation to be K\u2663 or KC")
        self.assertIn(repr(Card(12)), ['A\u2663', 'AC'], "expected representation to be A\u2663 or AC")

        "check comparisons"
        self.assertTrue(Card(0) < Card(51), "ordering failed")

    def test_02_points(self):
        "make a list of all the clubs (cards 0 to 12), check the points method on each card"
        cards = [Card(i) for i in range(13)]
        points = [0] * 9 + list(range(1,5))
        self.assertEqual(points, [x.points() for x in cards], "points incorrect")
    
    def test_03_blackjack_cards(self):
        "same as the earlier points test, but check BlackjackCard objects"
        cards = [BlackjackCard(i) for i in range(13)]
        self.assertEqual(0, cards[0].rank(), "expected blackjack rank to be 0")
        self.assertEqual(0, cards[0].suit(), "expected blackjack suit to be 0")
        points = [i+2 for i in range(9)] + [10,10,10,11]
        self.assertEqual(points, [x.points() for x in cards], "blackjack points incorrect")
