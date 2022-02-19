
def value_of_card(card):
    """Determine the scoring value of a card.
 
    :param card: str - given card.
    :return: int - value of a given card. 'J', 'Q', 'K' = 10; 'A' = 1; numerical value otherwise.
    """
    if card == 'J' or card == 'Q' or card == 'K':
        card = 10
    elif card == 'A':
        card = 1
    else:
        card = int(card)
    return int(card)
    
    
def higher_card(card_one, card_two):
    """Determine which card has a higher value in the hand.
 
    :param card_one, card_two: str - cards dealt. 'J', 'Q', 'K' = 10; 'A' = 1; numerical value otherwise.
    :return: higher value card - str. Tuple of both cards if they are of equal value.
    """
    if card_one == card_two or value_of_card(card_one)== value_of_card(card_two):
        return (card_one,card_two)
    if (value_of_card(card_one)> value_of_card(card_two)):
        return card_one
    if  value_of_card(card_two) > value_of_card(card_one):
        return card_two
    pass
def value_of_ace(card_one, card_two):
    """Calculate the most advantageous value for the ace card.
 
    :param card_one, card_two: str - card dealt. 'J', 'Q', 'K' = 10;
           'A' = 11 (if already in hand); numerical value otherwise.
 
    :return: int - value of the upcoming ace card (either 1 or 11).
    """
    if card_one == 'A' :
        return 1
    elif card_two == 'A':
        return 1