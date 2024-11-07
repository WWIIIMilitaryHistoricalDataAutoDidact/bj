import random
# 2nd commit
# 3rd commit
card_types = [
    'Hearts',
    'Diamonds',
    'Clubs',
    'Spades'
    ]
card_numbers = [
    'Ace',
    '2',
    '3',
    '4',
    '5',
    '6',
    '7',
    '8',
    '9',
    '10',
    'Jack',
    'Queen',
    'King'
    ]
deck = [[card_type,card_number] for card_type in card_types for card_number in card_numbers]
#print(deck)

def card_to_number(card):
    if (card[1] in ['Jack','Queen','King']):
        card_value = 10
    elif (card[1] in ['Ace']):
        card_value = 11
    else:
        card_value = card[1]
    return card_value

#print(deck[11])
#print(card_to_number(deck[11]))

def player_initial_cards():
    player_cards = []
    player_cards.append(random.choice(deck))
    player_cards.append(random.choice(deck))
    return player_cards

def total_value_initial_cards(player_cards):
    player_total = int(card_to_number(player_cards[0]))# + int(card_to_number(player_cards[1]))
    return player_total


print("Welcome to Black Jack. Begin y/n?:")
x = input()
if x == "y":
    player_cards = player_initial_cards()
    print("Your initial cards are: {first_card} and {second_card}".format(first_card=player_cards[0],second_card=player_cards[1])) 
    print("The total value of your cards is",  int(card_to_number(player_cards[0]))+int(card_to_number(player_cards[1])))

print("Add card? y/n:")
y = input()
if y == "y":
    player_cards.append(random.choice(deck))
    print("Your cards are now: {first}, {second}, {third}".format(first=player_cards[0],second=player_cards[1],third=player_cards[2]))
    your_score = int(card_to_number(player_cards[0]))+int(card_to_number(player_cards[1]))+ int(card_to_number(player_cards[2]))
    print("The total value of your cards is now", your_score )
else:
    your_score = int(card_to_number(player_cards[0]))+int(card_to_number(player_cards[1]))
    print("Your final score is",your_score)

if your_score > 21:
    print("Your score is greater than 21, you lose")
else:
    print("Are you sure? Add card? y/n:")
    z = input()
    if z == "y":
        player_cards.append(random.choice(deck))
        print("Your cards are now: {first}, {second}, {third}, {fourth}".format(first=player_cards[0],second=player_cards[1],third=player_cards[2],fourth=player_cards[3]))
        your_score = int(card_to_number(player_cards[0]))+int(card_to_number(player_cards[1]))+ int(card_to_number(player_cards[2]))+int(card_to_number(player_cards[3]))
        print("The total value of your cards is now", your_score )

    if your_score > 21:
        print("Your score is greater than 21, you lose")

    dealers_cards = player_initial_cards()
    print("Dealer's cards: {first} and {second}".format(first=dealers_cards[0],second=dealers_cards[1]))
    dealers_score = int(card_to_number(dealers_cards[0]))+int(card_to_number(dealers_cards[1]))
    print("The total value of the dealer's cards is", dealers_score )

    if dealers_score < 17:
        dealers_cards.append(random.choice(deck))
    print("Dealer Draws. Dealer's cards: {first}, {second}, {third}".format(first=dealers_cards[0],second=dealers_cards[1],third=dealers_cards[2]))
    dealers_score = int(card_to_number(dealers_cards[0]))+int(card_to_number(dealers_cards[1]))+int(card_to_number(dealers_cards[2]))
    print("The total value of the dealer's cards is now", dealers_score )
    if dealers_score > 21:
        print

    if (your_score <= 21) and (dealers_score < 21):
        if dealers_score > your_score:
            print("You lose!")
        elif dealers_score < your_score:
            print("You won!")
        else:
            print("It's a tie.")
    elif (your_score <= 21) and (dealers_score > 21):
        print("You won!")
    elif (your_score > 21) and (dealers_score > 21):
        print("It's a tie. No one wins")