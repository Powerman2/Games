import random


suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,'Queen':10, 'King':10, 'Ace':11}
playing = True

class Card:
#didd

	def __init__(self, suit, rank):
		self.suit = suit
		self.rank = rank
	def __str__(self):
		return self.rank + " of " + self.suit

class Deck:
	

	def __init__(self):
		self.deck = []  # start with an empty list
		for suit in suits:
			for rank in ranks:
				self.deck.append(Card(suit,rank))
                
	def __str__(self):
		x = ''
		for c in self.deck:
			x += str(c) + '\n '
		return x
	def shuffle(self):
		random.shuffle(self.deck)
	def deal(self):
		return self.deck.pop()
class Hand:
	def __init__(self):
		self.cards = []
		self.value = 0
		self.aces = 0
	def addCard(self, card):
		self.value+=values[card.rank]
		self.cards.append(str(card))
		if(card.rank == 'Ace'):
			self.aces+=1
	def adjustAce(self):
		while(self.aces >0 and self.value > 21):
			
			self.value - 10
			self.aces-=1
class Chips:
	def __init__(self):
		self.total = 0
		self.bet = 0
	def win(self):
		self.total+=self.bet
	def lose(self):
		self.total-=self.bet
def addMoney(chips):
	hold = 0
	while True:
		try:
			hold = int(input("How much money do you want to add? "))
		except ValueError:
			print("Please enter an integer value")
		else:
			if(hold < 0):
				print("Please enter a positive number")
			else:
				chips.total+=hold
				break
		
def takeBet(chips):
	while True:
		try:
			chips.bet = int(input("How much money do you want to bet? "))
		except ValueError:
			print("Please enter an integer value")
		else:
			if(chips.bet > chips.total):
				print("Your bet can't exceed", chips.total)
				chips.bet = 0
			else:
				break
def hit(deck, hand):
	hand.addCard(deck.deal())
	hand.adjustAce()
def ask(deck, hand):
	global playing
	while True:
		x = input("Would you like to hit or stay? ('s' or 'h'): ")
		if(x.lower() == 'h'):
			hit(deck,hand)
		elif(x.lower() == 's'):
			playing = False
			print('Dealer is now playing')
		else:
			print('Enter s or h')
			continue
		break
def show_some(player,dealer):
	print("\nDealer's Hand:")
	print(" <card hidden>")
	print('',dealer.cards[1])  
	print("\nPlayer's Hand:", *player.cards, sep='\n ')
    
def show_all(player,dealer):
	print("\nDealer's Hand:", *dealer.cards, sep='\n ')
	print("Dealer's Hand =",dealer.value)
	print("\nPlayer's Hand:", *player.cards, sep='\n ')
	print("Player's Hand =",player.value)
    
def player_busts(player,dealer,chips):
	print("Player busts!")
	chips.lose()

def player_wins(player,dealer,chips):
	print("Player wins!")
	chips.win()

def dealer_busts(player,dealer,chips):
	print("Dealer busts!")
	chips.win()
    
def dealer_wins(player,dealer,chips):
	print("Dealer wins!")
	chips.lose()
    
def push(player,dealer):
	print("Dealer and Player tie! It's a push.")
    
chips = Chips()
while True:
	print("Welcome")
	deck = Deck()
	deck.shuffle()

	player = Hand()
	player.addCard(deck.deal())
	player.addCard(deck.deal())

	dealer = Hand()
	dealer.addCard(deck.deal())
	dealer.addCard(deck.deal())

	
	addMoney(chips)
	takeBet(chips)

	show_some(player, dealer)
	while playing:  # recall this variable from our hit_or_stand function
        
        # Prompt for Player to Hit or Stand
		ask(deck,player)
		show_some(player,dealer)

		if player.value > 21:
			player_busts(player,dealer,chips)
			break
    
    # If Player hasn't busted, play Dealer's hand        
	if player.value <= 21:
        
		while dealer.value < 17:
			hit(deck,dealer)
            
        # Show all cards
		show_all(player,dealer)
        
        # Test different winning scenarios
		if dealer.value > 21:
			dealer_busts(player,dealer,chips)

		elif dealer.value > player.value:
			dealer_wins(player,dealer,chips)

		elif dealer.value < player.value:
			player_wins(player,dealer,chips)

		else:
			push(player,dealer)

    # Inform Player of their chips total    
	print("\nPlayer's winnings stand at",chips.total)
    
    # Ask to play again
	new_game = input("Would you like to play another hand? Enter 'y' or 'n' ")
	if new_game[0].lower()=='y':
		playing=True
		continue
	else:
		print("Thanks for playing!")
		break
