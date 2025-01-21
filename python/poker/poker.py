import sys
from collections import Counter, defaultdict, namedtuple
from enum import IntEnum, auto

CARD_RANKS = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A")


class PokerHandType(IntEnum):
    HIGH_CARD = auto()
    ONE_PAIR = auto()
    TWO_PAIR = auto()
    THREE_OF_A_KIND = auto()
    STRAIGHT = auto()
    FLUSH = auto()
    FULL_HOUSE = auto()
    FOUR_OF_A_KIND = auto()
    STRAIGHT_FLUSH = auto()


class CardRankValueCounter(Counter):  # pylint: disable=abstract-method
    def rank_values_with_count_equal_to(self, count):
        return sorted((key for key in self if self[key] == count), reverse=True)

    def rank_values_with_count_not_equal_to(self, count):
        return sorted((key for key in self if self[key] != count), reverse=True)


PokerHand = namedtuple("PokerHand", ("type", "strength_within_type"))


def best_hands(hands):
    hands_per_poker_hand = defaultdict(list)
    for hand in hands:
        hands_per_poker_hand[strongest_possible_poker_hand(hand)].append(hand)
    return hands_per_poker_hand[max(hands_per_poker_hand)]


def strongest_possible_poker_hand(hand):
    for poker_hand_type in sorted(PokerHandType, reverse=True):
        if poker_hand := vars(sys.modules[__name__])[poker_hand_type.name.lower()](
            hand
        ):
            return poker_hand
    return None


def straight_flush(hand):
    if (straight_hand := straight(hand)) and flush(hand):
        return PokerHand(
            PokerHandType.STRAIGHT_FLUSH, straight_hand.strength_within_type
        )
    return None


def four_of_a_kind(hand):
    return n_of_a_kind(hand, 4, PokerHandType.FOUR_OF_A_KIND)


def full_house(hand):
    card_rank_counter = count_hand_cards_rank_values(hand)
    if set(card_rank_counter.values()) == {3, 2}:
        return PokerHand(
            PokerHandType.FULL_HOUSE,
            tuple(
                card_rank_counter.rank_values_with_count_equal_to(3)
                + card_rank_counter.rank_values_with_count_equal_to(2)
            ),
        )
    return None


def flush(hand):
    suit_counter = count_card_suits(hand)
    if len(set(suit_counter)) == 1:
        return PokerHand(PokerHandType.FLUSH, tuple(hand_cards_rank_values(hand)))
    return None


def straight(hand):
    card_rank_counter = count_hand_cards_rank_values(hand)
    if len(set(card_rank_counter.values())) == 1:
        if set(hand_cards_ranks(hand)) == {"A", "2", "3", "4", "5"}:
            return PokerHand(PokerHandType.STRAIGHT, (5,))
        if ((max_card_rank := max(card_rank_counter)) - min(card_rank_counter)) == 4:
            return PokerHand(PokerHandType.STRAIGHT, (max_card_rank,))
    return None


def three_of_a_kind(hand):
    return n_of_a_kind(hand, 3, PokerHandType.THREE_OF_A_KIND)


def two_pair(hand):
    card_rank_counter = count_hand_cards_rank_values(hand)
    if sum(count == 2 for count in card_rank_counter.values()) == 2:
        return PokerHand(
            PokerHandType.TWO_PAIR,
            tuple(
                card_rank_counter.rank_values_with_count_equal_to(2)
                + card_rank_counter.rank_values_with_count_not_equal_to(2)
            ),
        )
    return None


def one_pair(hand):
    return n_of_a_kind(hand, 2, PokerHandType.ONE_PAIR)


def high_card(hand):
    return PokerHand(PokerHandType.HIGH_CARD, tuple(hand_cards_rank_values(hand)))


def n_of_a_kind(hand, count, poker_hand_type):
    card_rank_counter = count_hand_cards_rank_values(hand)
    if count in card_rank_counter.values():
        return PokerHand(
            poker_hand_type,
            tuple(
                card_rank_counter.rank_values_with_count_equal_to(count)
                + card_rank_counter.rank_values_with_count_not_equal_to(count)
            ),
        )
    return None


def rank_of(card):
    return card[:-1]


def suit_of(card):
    return card[-1]


def hand_cards_ranks(hand):
    return (rank_of(card) for card in hand.split())


def hand_cards_rank_values(hand):
    return sorted(
        (CARD_RANKS.index(rank_of(card)) + 2 for card in hand.split()), reverse=True
    )


def count_hand_cards_rank_values(hand):
    return CardRankValueCounter(hand_cards_rank_values(hand))


def count_card_suits(hand):
    return Counter(suit_of(card) for card in hand.split())
