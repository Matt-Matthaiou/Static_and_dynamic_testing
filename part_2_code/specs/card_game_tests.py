import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):

    def setUp(self):
        self.card1 = Card('spades', 1)
        self.card2 = Card('Hearts', 10)

    def test_check_for_ace(self):
        result = CardGame.check_for_ace(self, self.card1)
        self.assertEqual(result, True)

    def test_highest_card(self):
        result = CardGame.highest_card(self, self.card1, self.card2)
        self.assertEqual(result, self.card2)

    def test_cards_total(self):
        cards = [self.card1, self.card2]
        result = CardGame.cards_total(self, cards)
        self.assertEqual(result, "You have a total of 11")