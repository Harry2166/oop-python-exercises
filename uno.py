
import random
import time

class Card:

    '''
    Represents an individual card
    '''

    def __init__(self, colors=0, roles=3, special_card=2):
        self.colors = colors
        self.roles = roles
        self.special_card = special_card

    color_names = ['blue', 'green', 'yellow', 'red', ' ']
    role_names = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "draw_two", "reverse", "skip", ' ']
    special_cards_names = ["wild", "wild_draw_four", ' ']

    def __str__(self):
        return '(%s, %s, %s)' % (Card.color_names[self.colors],
        Card.role_names[self.roles], Card.special_cards_names[self.special_card])

class Deck:
    
    '''
    Represents the deck of uno cards
    '''

    ''''
    This pile list is where the representation of where the uno cards will be placed 
    '''

    pile = []

    def __init__(self):
        self.cards = []
        for i in range(2): # done twice so that each card here will have a copy
            for color in range(4): # this is meant for the indexes of the colors list
                for role in range(0, 13): # this is meant for the indexes of the roles list
                    card = Card(color, role)
                    self.cards.append(card)

        for i in range(4): # done four times because there are 8 wild cards in total
            for j in range(2): # this is meant for the indexes of the special_card list
                card=Card(-1, -1, j)
                self.cards.append(card)

        self.result = [] # this is where the cards will stay
        for card in self.cards:
            self.result.append((card))

    def __str__(self):
        return f'{[str(item) for item in self.result]}'

    def shuffle(self):
        random.shuffle(self.result)
        return f'{[str(item) for item in self.result]}'

    def remove_card(self):
        if len(self.result) == 0: # this if statement is in the case that the self.result list runs 
                                  # out cards to get from.
            self.result = self.pile
            self.pile = []
        return self.result.pop()

    def draw_card(self, card):
        return self.cards.append(card)

class Hand(Deck):
    '''
    Represents the hand of a playing card
    '''
    def __init__(self, label=''):
        self.cards = []
        self.label = label

    def draw_from_pile(self):
        return self.cards.append(self.pile.pop())

    def put_card_to_pile(self):
        return self.pile.append(self.cards.pop())

    def __str__(self):
        return f'{[str(item) for item in self.cards]}'

def add_amount_of_cards(x, hand, deck):
    for i in range(x):
        hand.cards.append(deck.result.pop())

def winner(hand, list_of_players): # this function will be used to determine the winner
    if len(hand.cards) == 0 or len(list_of_players) == 1:
        print(f"{hand.label} is the winner!")
        return True

def skip_player():
    skip_player.has_been_called = True # this function will be used to determine if a skip card 
                                       # has been dropped.

def reverse_card(l, hand_number):
    index = l.index(hand_number)
    reversed_list = t[index-1::-1] + t[-1:index-1:-1] # this reverses the list so that the person who dropped the
                                                      # reverse card will be the last and the person who came before
                                                      # them will be the first on the nexxt list.
    reverse_card.has_been_called = True # this part is similar to the previous function while will be used to  
                                        # determine if a reverse card has been dropped.
    return reversed_list


print("======================================================================================================")

deck1 = Deck()
deck1.pile
deck1.shuffle()

t = list()

# this part of code determines the players of the game
number_of_players = int(input("How many players are gonna play?\n"))
count = 0
while count != number_of_players:
    name = input(f'Place your name (Player{count+1})!\n')
    t.append(Hand(name))
    count += 1

# this for loop distributes the cards from the self.result list to the players of the game
for i in range(7):
    for i in range(len(t)):
        chord = deck1.remove_card()
        t[i].draw_card(chord)

def action_1(deck, card_place, hand_number, l): 
    if hand_number.cards[card_place - 1].roles > 9: # 10 = "draw_two", 11 = "reverse", 12 = "skip"
        index = l.index(hand_number)
        index_2 = len(l) - 1
        if hand_number.cards[card_place - 1].roles == 10:
            deck.pile.append(hand_number.cards.pop(card_place - 1))
            if index == index_2:
                for i in range(2):
                    l[0].cards.append(deck.result.pop())
                    print(f'The card of {l[0].label} cards are NOW: ')
                    print(l[0])
            else:
                for i in range(2):
                    l[index+1].cards.append(deck.result.pop())
                print(f'The card of  {l[index+1].label} are NOW: ')
                print(l[index+1])
        elif hand_number.cards[card_place - 1].roles == 11:
            deck.pile.append(hand_number.cards.pop(card_place - 1))
            reverse_card(l, hand_number)
        else:
            placed = hand_number.cards.pop(card_place - 1)
            deck.pile.append(placed)
            skip_player()
    else:
        placed = hand_number.cards.pop(card_place - 1)
        deck.pile.append(placed)

def wild_card_function(deck, hand_number, card_place, l): #"wild" 0, "wild_draw_four" 1
    index_2 = len(l) - 1
    if hand_number.cards[card_place - 1].special_card == 0:
        print("You may place any card of any color and role this turn!")
    elif hand_number.cards[card_place - 1].special_card == 1:
        index = l.index(hand_number)
        if index == index_2:
            for i in range(4):
                l[0].cards.append(deck.result.pop())
            print(f'The card of {l[0].label} are NOW: ')
            print(l[0])
        else:
            for i in range(4):
                l[index+1].cards.append(deck.result.pop())
            print(f'The card of {l[index+1].label} are NOW: ')
            print(l[index+1])

def draw_a_card(deck, hand_number):
    kard = deck.remove_card()
    hand_number.draw_card(kard)
    print("Your cards are NOW: ")
    print(hand_number)

skip_player.has_been_called = False # the function will be called before the main function to allow it to function.
                                    # see line 207 for reasoning

def main(deck, list_players):
    # a while loop that let's the player pick what they want to do
    deck.pile.append(deck.result.pop())
    if deck.pile[-1].colors == 0 and deck.pile[-1].roles == 0 and deck.pile[-1].special_card != None:
        deck.pile.append(deck.result.pop())
    game = True
    while game:
        print(f"Order of players: ")
        cards_on_deck = len(deck.result)
        print(cards_on_deck)
        for player in list_players:
            print(player.label)
        for player in list_players:
            print(f"It is {player.label}'s turn!")
            if len(deck.pile) > 0:
                print(f'The last card placed was: {deck.pile[-1]}')
            else:
                print(f'The last card placed was: {None}')
            print("Your cards are: ")
            print(player)
            action = int(input("What do you want to do?\nPress 1 to place a card\nPress 2 to get a card\nPress 3 if you have been skipped\n"))
            if skip_player.has_been_called: # without line 181 being called, the whole main function will not work because 
                                            # skip_player() has not been called yet and skip_player.has_been_called will
                                            # not have a value
                action = 0
                while action != 3:
                    action = int(input("You have been skipped. Please type 3: "))
                skip_player.has_been_called = False
            elif action == 1:
                place_card = int(input("Which card you like to place? Enter its number on the list. Type 505 if you made a mistake and would like to draw a card.\n"))
                if place_card == 505:
                    draw_a_card(deck, player)
                else: # we can only place a card if it has the same color, same role, or a wild card
                    reverse_card.has_been_called = False
                    if (player.cards[place_card - 1].colors ==  deck.pile[-1].colors):
                        action_1(deck, place_card, player, list_players)
                        if reverse_card.has_been_called:
                            list_players = reverse_card(list_players, player)
                            break
                    elif (player.cards[place_card - 1].roles == deck.pile[-1].roles):
                        action_1(deck, place_card, player, list_players)
                        if reverse_card.has_been_called:
                            list_players = reverse_card(list_players, player)
                            break
                    elif (player.cards[place_card - 1].colors == -1 and player.cards[place_card - 1].roles == -1 and player.cards[place_card - 1].special_card != None):
                            wild_card_function(deck, player, place_card, list_players)
                            placed = player.cards.pop(place_card - 1)
                            deck.pile.append(placed)
                    elif (deck.pile[-1].colors == -1 and deck.pile[-1].roles == -1 and deck.pile[-1].special_card != None):
                            placed = player.cards.pop(place_card - 1)
                            deck.pile.append(placed)
                    else:
                        print("invalid turn")
            elif action == 2:
                draw_a_card(deck, player)
            if winner(player, list_players):
                game = False
                break

main(deck1, t)