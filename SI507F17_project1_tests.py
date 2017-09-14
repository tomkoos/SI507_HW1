# Do not change import statements.
import unittest
from SI507F17_project1_cards import *
from helper_functions import *

# Write your unit tests to test the cards code here.
'''
You should test to ensure that everything explained in the code description
file works as that file says.
'''
'''
If you have correctly written the tests, at least 3 tests should fail. If more
than 3 tests fail, it should be because multiple of the test methods address
the same problem in the code.
'''
'''
You may write as many TestSuite subclasses as you like, but you should try to
make these tests well-organized and easy to read the output.
'''
# You should invoke the tests with verbosity=2 (make sure you invoke them!)

###########


def setOfAllCards():
    suit_names = ['Diamonds', 'Clubs', 'Hearts', 'Spades']
    return set([(suit, rank) for suit in suit_names for rank in range(1, 14)])


class Test_Card(unittest.TestCase):
    def setUp(self):
        self.NumToSuit = {0: 'Diamonds', 1: 'Clubs', 2: 'Hearts', 3: 'Spades'}
        self.faces = [(1, 'Ace'), (11, 'Jack'), (12, 'Queen'), (13, 'King')]
        self.NumToRank = dict([(x, x) for x in range(2, 14)] + self.faces)

    def test_private_variable(self):
        card = Card()
        self.assertEqual(
            card.suit_names, ['Diamonds', 'Clubs', 'Hearts', 'Spades'],
            "Test: initializing Card.suit_names correctly")
        self.assertEqual(
            card.rank_levels, list(range(1, 14)),
            "Test: initializing Card.rank_levels correctly")
        self.assertEqual(
            card.faces, {1: "Ace", 11: "Jack", 12: "Queen", 13: "King"},
            "Test: initializing Card.faces correctly")

    def test_init(self):
        card = Card()
        self.assertEqual(card.suit, 'Diamonds',
                         "Test: Card() initialize the value of Card.suit"
                         "to 'Diamonds'")
        self.assertEqual(card.rank, 2,
                         "Test: Card() initialize the value of Card.rank to 2")
        self.assertEqual(card.rank_num, 2,
                         "Test: Card() initialize the value of Card.rank_num"
                         "to 2")
        # Test initializion for all possible cards
        for suit_num in range(4):
            for rank_num in range(1, 14):
                card = Card(suit_num, rank_num)
                self.assertEqual(card.suit, self.NumToSuit[suit_num],
                                 "Test: Card(suit = {}, rank_num = {}), "
                                 "Card.suit should be {}"
                                 .format(suit_num, rank_num,
                                         self.NumToSuit[suit_num]))
                self.assertEqual(card.rank, self.NumToRank[rank_num],
                                 "Test: Card(suit = {}, rank_num = {}), "
                                 "Card.rank should be {}"
                                 .format(suit_num, rank_num,
                                         self.NumToRank[rank_num]))
                self.assertEqual(card.rank_num, rank_num,
                                 "Test: Card(suit = {}, rank_num = {}), "
                                 "Card.rank_num should be {}"
                                 .format(suit_num, rank_num, rank_num))

    def test_print(self):
        # Test print method for all possible cards
        for suit_num in range(4):
            for rank_num in range(1, 14):
                card = Card(suit_num, rank_num)
                self.assertEqual(card.__str__(), '{} of {}'
                                 .format(self.NumToRank[rank_num],
                                         self.NumToSuit[suit_num]),
                                 "Test: Card(suit = {}, rank = {}), "
                                 "print method should output '{} of {}'"
                                 .format(suit_num, rank_num,
                                         self.NumToRank[rank_num],
                                         self.NumToSuit[suit_num]))


class Test_Deck(unittest.TestCase):
    def test_init(self):
        deck = Deck()
        self.assertIsInstance(deck.cards, list,
                              "Test: Deck() should return an object "
                              "of class list")
        self.assertEqual(len(deck.cards), 52,
                         "Test: Deck() should return an object of length 52")
        AllCards = setOfAllCards()
        for card in deck.cards:
            cardTuple = (card.suit, card.rank_num)
            self.assertIn(cardTuple, AllCards,
                          "Test: Deck().cards should have all the cards "
                          "with no duplicates")
            AllCards.remove(cardTuple)

    def test_pop_card(self):
        deck = Deck()
        popped_card = deck.pop_card()
        self.assertIsInstance(popped_card, Card,
                              "Test: pop_card() should return an object "
                              "of class Card")
        self.assertEqual(len(deck.cards), 51,
                         "Test: popped out one card using pop_card(), "
                         "deck size should be decreased to 51")
        self.assertEqual(popped_card.rank, 'King',
                         "Test: pop_card() should return the last card of "
                         "the deck, this card should have rank 'King'")
        self.assertEqual(popped_card.suit, 'Spades',
                         "Test: pop_card() should return the last card of "
                         "the deck, this card should have suit 'Spades'")

        popped_card = deck.pop_card(0)
        self.assertEqual(len(deck.cards), 50,
                         "Test: popped out card the second time, "
                         "deck size should be decreased to 50")
        self.assertEqual(popped_card.rank, 'Ace',
                         "Test: pop_card(0) should return the first card of "
                         "the deck, this card should have rank 'Ace'")
        self.assertEqual(popped_card.suit, 'Diamonds',
                         "Test: pop_card(0) should return the first card of "
                         "the deck, this card should have suit 'Diamonds'")

        deck = Deck()
        for i in range(52):
            deck.pop_card()
        self.assertEqual(not deck.cards, True,
                         "Test: should be able to pop_card() 52 times "
                         "when a deck has 52 cards")

    def test_shuffle(self):
        # Test for full deck
        sortedDeck = Deck()
        deck = Deck()
        random.seed(0)
        deck.shuffle()
        self.assertEqual(deck.shuffle(), None,
                         "Test: Deck.shuffle() should return nothing (None)")
        self.assertEqual(len(deck.cards), 52,
                         "Test: after shuffling a deck, "
                         "deck size should not change, in this case 52")
        AllCards = setOfAllCards()
        for card in deck.cards:
            cardTuple = (card.suit, card.rank_num)
            self.assertIn(cardTuple, AllCards,
                          "Test: Deck().cards should have all the cards "
                          "with no duplicates")
            AllCards.remove(cardTuple)

        flag = False
        for i in range(len(deck.cards)):
            if (sortedDeck.cards[i].__str__() != deck.cards[i].__str__()):
                flag = True
                break
        self.assertTrue(flag, "Test: Deck.shuffle() should randomly shuffled "
                        "the deck, not just do nothing")

        # Test for partial deck
        sortedDeck = Deck()
        sortedDeck.pop_card(5)
        deck = Deck()
        deck.pop_card(5)
        random.seed(0)
        deck.shuffle()
        flag = False
        for i in range(len(deck.cards)):
            if (sortedDeck.cards[i].__str__() != deck.cards[i].__str__()):
                flag = True
                break
        self.assertTrue(flag, "Test: Deck.shuffle() should randomly shuffled "
                        "the deck, not just do nothing")

    def test_replace_card(self):
        deck = Deck()
        card1 = Card(2, 11)
        self.assertEqual(deck.replace_card(card1), None,
                         "Test: Deck.replace_card(input) "
                         "should return nothing (None)")
        deck.replace_card(card1)
        self.assertEqual(len(deck.cards), 52,
                         "Test: start with a full deck. "
                         "replacing the card that's already in "
                         "a deck should not change deck size")
        deck.pop_card()
        deck.replace_card(card1)
        self.assertEqual(len(deck.cards), 51,
                         "Test: start with a partial deck. "
                         "replacing the card that's already in "
                         "a deck should not change deck size")

        deck = Deck()
        popped_card = deck.pop_card()
        listOfCards = [card.__str__() for card in deck.cards]
        self.assertNotIn(popped_card.__str__(), listOfCards,
                         "Test: the popped card should no longer "
                         "be in the deck")
        deck.replace_card(popped_card)
        self.assertEqual(len(deck.cards), 52,
                         "Test: start with a partial deck. "
                         "replacing the card that's not in "
                         "a deck should increase deck size by one")
        listOfCards = [card.__str__() for card in deck.cards]
        self.assertIn(popped_card.__str__(), listOfCards,
                      "Test: replacing the card that is not in the deck, "
                      "the card should be added back to the deck")

    def test_sort_cards(self):
        # Test for full deck
        sortedDeck = Deck()
        deck = Deck()
        deck.shuffle()
        deck.sort_cards()
        for i in range(52):
            self.assertEqual(deck.cards[i].__str__(), sortedDeck.cards[i].__str__(),
                             "Test: after sorting, the cards should be "
                             "in a correct order")
        # Test for partial deck
        deck = Deck()
        for i in range(10):
            deck.shuffle()
            deck.pop_card()
        deck.sort_cards()
        self.assertEqual(len(deck.cards), 40,
                         "Test: after sorting the remaining cards, "
                         "the deck size should not be affected")

    def test_deal_hand(self):
        deck = Deck()
        hand = deck.deal_hand(hand_size=5)
        self.assertIsInstance(hand, list,
                              "Test: Deck().deal_hand should return an object "
                              "of class list")
        self.assertEqual(len(hand), 5,
                         "Test: Deck().deal_hand should return an object of "
                         "length equal to a value of hand_size")
        self.assertEqual(len(deck.cards), 47,
                         "Test: after dealing a hand, length of Deck().cards "
                         "or the number of remaining cards should be changed "
                         "accordingly")

        deck = Deck()
        hand = deck.deal_hand(hand_size=52)
        self.assertIsInstance(hand, list,
                              "Test: Deck().deal_hand should return an object "
                              "of class list")
        self.assertEqual(len(hand), 52,
                         "Test: Deck().deal_hand should return an object of "
                         "length equal to a value of hand_size")
        self.assertEqual(len(deck.cards), 0,
                         "Test: after dealing a hand, length of Deck().cards "
                         "or the number of remaining cards should be changed "
                         "accordingly")


class Test_play_war_game(unittest.TestCase):
    def test_return(self):
        play = play_war_game(testing=True)
        self.assertIsInstance(play, tuple,
                              "Test: play_war_game() should return an object "
                              "of class tuple")
        self.assertEqual(len(play), 3,
                         "Test: length of the return object should equal to 3")
        self.assertIn(play[0], {'Player1', 'Player2', 'Tie'},
                      "Test: value of the first item in the tuple should be "
                      "either 'Player1', 'Player2' or 'Tie'")
        self.assertIsInstance(play[1], int,
                              "Test: value of the second item in the tuple "
                              "should be int")
        self.assertIsInstance(play[2], int,
                              "Test: value of the third item in the tuple "
                              "should be int")


class Test_show_song(unittest.TestCase):
    def test_return(self):
        self.assertIsInstance(show_song(), Song,
                              "Test: show_song(input) should return an object "
                              "of class Song")

    def test_search(self):
        self.assertTrue(show_song('Random'),
                        "Test: should be able to search for any search term")


unittest.main(verbosity=2)
