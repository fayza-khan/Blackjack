import random
suit_cards = ['Spades', 'Clubs', 'Hearts', 'Diamonds']
value_cards = ["A", 'K', 'Q', 'J', 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Defined a function for choosing a card at random


def random_cards():
    random_suit = random.choice(suit_cards)
    random_value = random.choice(value_cards)
    print(random_value, "of", random_suit)
    return random_value
# Creating a class for the player to add his attribute of balance for betting.


class Player:

    def __init__(self, coins):
        self.coins = coins
        self.name = input("Player enter your name:\n")

    def __str__(self):
        return "{} has balance of {} coins.".format(self.name, self.coins)

    def __len__(self):
        return self.coins
# Creating a class for all activities in the game including functions of hit and stay


class ChoicesInBlackJack:
    def hit(self):
        return random_cards()

    def stay(self):
        print("Player want to stay!")


class BlackJack(Player, ChoicesInBlackJack):

    player_total = 0
    dealer_total = 0

    def __init__(self, available_chips, dealer_name):

        ChoicesInBlackJack.__init__(self)
        self.dealer_name = dealer_name

        print("Welcome to the Black Jack game!!!")
        Player.__init__(self, available_chips)
        name_of_player = self.name

        print("Your dealer for the day is", self.dealer_name, "!")
        while True:
            try:
                betting_amount = int(input("\nPlayer {} please enter your betting amount:".format(name_of_player)))
                if betting_amount > available_chips:
                    print("Not valid bet! Amount in betting is greater than your available balance chips.")
                    continue
                else:
                    print("Betting amount is {}!".format(betting_amount))
                    break
            except:
                print("Please enter an integer value!")
        self.betting_amount = betting_amount

    def check_for_player(self, card_value, total_value):
        if card_value in range(2, 11):
            total_value += card_value
        elif card_value == "Q" or card_value == "K" or card_value == "J":
            total_value += 10
        else:
            ace = int(input("What value of ace you want? 1 or 11:"))
            total_value += ace
        return total_value

    def initial_cards_player(self):
        print("\nPlayer your two up cards are:")
        card1 = random_cards()
        card2 = random_cards()
        x = BlackJack.check_for_player(self, card1, self.player_total)
        y = BlackJack.check_for_player(self, card2, self.player_total)
        self.player_total = x + y
        return "Player {} total at starting is {}".format(self.name, self.player_total)

    def initial_cards_dealer(self):
        print("\nDealer your one up card is:")
        card3 = random_cards()
        print("<Hidden Card>")
        x = BlackJack.check_for_player(self, card3, self.dealer_total)
        self.dealer_total += x

    def rounds_player(self):
        print("\nPlayer", self.name, "your chance first!")

        print(BlackJack.initial_cards_player(self))
        BlackJack.initial_cards_dealer(self)

        while True:
            if self.player_total > 21:
                print("Player busted!")
                break
            elif self.player_total == 21:
                break
            choice_game = input("\n{} What do you want to do? Hit or Stay:".format(self.name)).lower()
            if choice_game == "hit":
                x = ChoicesInBlackJack.hit(self)
                self.player_total = BlackJack.check_for_player(self, x, self.player_total)
                print("\n{} is player's total".format(self.player_total))
            else:
                ChoicesInBlackJack.stay(self)
                break
        return self.player_total

    def rounds_dealer(self):
        print("\nHidden card of dealer is:")
        hidden_card = random_cards()
        if hidden_card in range(2, 11):
            self.dealer_total += hidden_card
        elif hidden_card == "Q" or hidden_card == "K" or hidden_card == "J":
            self.dealer_total += 10
        else:
            ace = int(input("What value of ace you want? 1 or 11:"))
            self.dealer_total += ace
        print("Dealer {} total at starting is {}".format(self.dealer_name, self.dealer_total))
        while True:
            if self.player_total < 21:
                if self.dealer_total >= 17:
                    break
                choice_game = input(
                    "Dealer {} your chance now as the player has stayed! Type hit:".format(self.dealer_name)).lower()
                if choice_game == "hit":
                    x = ChoicesInBlackJack.hit(self)
                    self.dealer_total = BlackJack.check_for_player(self, x, self.dealer_total)
                    print("{} is dealer's total".format(self.dealer_total))
                else:
                    break
            else:
                break
        return self.dealer_total

    def result(self):
        count1 = BlackJack.rounds_player(self)
        count2 = BlackJack.rounds_dealer(self)
        bal = 0
        if count1 == 21 or (count2 > 21 and count1 < 21):
            print("Dealer busted!")
            print("Player {} is the winner!".format(self.name))
            bal += self.coins + self.betting_amount
        elif count2 == 21 or (count2 < 21 and count1 > 21):
            print("Dealer {} is the winner!".format(self.dealer_name))
            bal += self.coins - self.betting_amount
        print("\nThe available balance is", bal)
        if bal == 0 or bal < 0:
            print("Sorry you've lost the entire bet!\nOut of the game.\nNo coins left!")

            x = input("\n{} do you want to play again? Yes/No".format(self.name)).lower()
            if x == "yes" or x == "y":
                repeat = BlackJack(bal, self.dealer_name)
                repeat.result()
            else:
                print("No issue! Play another day!")
                return False


final = BlackJack(100, "Jack")
final.result()


