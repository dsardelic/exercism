"""Functions to help play and score a game of blackjack.

How to play blackjack:    https://bicyclecards.com/how-to-play/blackjack/
"Standard" playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
"""

TEN_CARDS = ["J", "Q", "K"]
ACE_LOWER_VALUE = 1
ACE_HIGHER_VALUE = 11
WINNING_SCORE = 21
DOUBLE_DOWN_LOWER_LIMIT = 9
DOUBLE_DOWN_UPPER_LIMIT = 11


def value_of_card(card):
    """Determine the scoring value of a card.

    :param card: str - given card.
    :return: int - value of a given card.  See below for values.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """

    if card in TEN_CARDS:
        return 10
    if card == "A":
        return 1
    return int(card)


def higher_card(card_one, card_two):
    """Determine which card has a higher value in the hand.

    :param card_one: str - cards dealt in hand.  See below for values.
    :param card_two: str - cards dealt in hand.  See below for values.
    :return: str or tuple - resulting Tuple contains both cards if they are of equal value.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """

    if value_of_card(card_one) > value_of_card(card_two):
        return card_one
    if value_of_card(card_one) < value_of_card(card_two):
        return card_two
    return card_one, card_two


def value_of_ace(card_one, card_two):
    """Calculate the most advantageous value for the ace card.

    :param card_one, card_two: str - card dealt. See below for values.
    :return: int - either 1 or 11 value of the upcoming ace card.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.
    """

    match (card_one, card_two):
        case ("A", "A"):
            return ACE_LOWER_VALUE
        case ("A", card) | (card, "A"):
            return (
                ACE_LOWER_VALUE
                if ACE_HIGHER_VALUE + value_of_card(card) + ACE_HIGHER_VALUE
                > WINNING_SCORE
                else ACE_HIGHER_VALUE
            )
        case _:
            return (
                ACE_LOWER_VALUE
                if value_of_card(card_one) + value_of_card(card_two) + ACE_HIGHER_VALUE
                > WINNING_SCORE
                else ACE_HIGHER_VALUE
            )


def is_blackjack(card_one, card_two):
    """Determine if the hand is a 'natural' or 'blackjack'.

    :param card_one, card_two: str - card dealt. See below for values.
    :return: bool - is the hand is a blackjack (two cards worth 21).

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.
    """

    match (card_one, card_two):
        case ("A", "A"):
            return False
        case ("A", card) | (card, "A"):
            return ACE_HIGHER_VALUE + value_of_card(card) == WINNING_SCORE
        case _:
            return value_of_card(card_one) + value_of_card(card_two) == WINNING_SCORE


def can_split_pairs(card_one, card_two):
    """Determine if a player can split their hand into two hands.

    :param card_one, card_two: str - cards dealt.
    :return: bool - can the hand be split into two pairs? (i.e. cards are of the same value).
    """

    if card_one in TEN_CARDS and card_two in TEN_CARDS:
        return True
    return card_one == card_two


def can_double_down(card_one, card_two):
    """Determine if a blackjack player can place a double down bet.

    :param card_one, card_two: str - first and second cards in hand.
    :return: bool - can the hand can be doubled down? (i.e. totals 9, 10 or 11 points).
    """

    match (card_one, card_two):
        case ("A", card) | (card, "A"):
            dealt_score = ACE_LOWER_VALUE + value_of_card(card)
        case _:
            dealt_score = value_of_card(card_one) + value_of_card(card_two)
    return DOUBLE_DOWN_LOWER_LIMIT <= dealt_score <= DOUBLE_DOWN_UPPER_LIMIT
