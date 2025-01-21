import collections

SINGLE_BOOK_PRICE = 800
DISCOUNT_PCTS = (0, 0, 5, 10, 20, 25)


def total(basket):
    if not basket:
        return 0.0
    bookset_sizes = collections.Counter()
    basket_counter = collections.Counter(basket)
    while basket_counter:
        bookset_sizes.update([len(basket_counter.keys())])
        basket_counter.subtract(basket_counter.keys())
        basket_counter = +basket_counter
    while bookset_sizes[3] and bookset_sizes[5]:
        bookset_sizes.subtract([3, 5])
        bookset_sizes.update([4, 4])
    return sum(
        bookset_size * SINGLE_BOOK_PRICE * (1 - DISCOUNT_PCTS[bookset_size] / 100) * qty
        for bookset_size, qty in bookset_sizes.items()
    )
