import functools
import itertools

SINGLE_BOOK_PRICE = 800
DISCOUNT_PCTS = (0, 0, 5, 10, 20, 25)


def total(basket):
    if not basket:
        return 0.0

    min_price = float("inf")

    def seek(basket, grouping_sizes, curr_price):
        nonlocal min_price
        assert bool(basket) == bool(grouping_sizes)
        if not basket:
            min_price = min(min_price, curr_price)
            return
        if curr_price >= min_price:
            return
        booksets = itertools.permutations(basket, grouping_sizes[0])
        for bookset in booksets:
            seek(
                remove_bookset_from_basket(bookset, basket),
                grouping_sizes[1:],
                curr_price + price_of_bookset(tuple(sorted(bookset))),
            )

    basket = sorted(basket)
    for grouping_sizes in book_grouping_sizes_generator(
        len(basket), len(DISCOUNT_PCTS) - 1
    ):
        seek(basket, grouping_sizes, 0.0)
    return min_price


def book_grouping_sizes_generator(books_count, max_grouping_size):
    def bgs(books_count, prev_grouping_sizes):
        if not books_count:
            yield prev_grouping_sizes
        else:
            for i in range(books_count, 0, -1):
                yield from bgs(books_count - i, prev_grouping_sizes + (i,))

    if books_count <= 0 or max_grouping_size <= 0:
        yield tuple()
    else:
        for i in range(min(books_count, max_grouping_size), 0, -1):
            yield from bgs(books_count - i, (i,))


def remove_bookset_from_basket(bookset, basket):
    new_basket = list(basket)
    for book in bookset:
        new_basket.remove(book)
    return new_basket


@functools.lru_cache(1000000)
def price_of_bookset(bookset):
    if not bookset:
        return 0.0
    distinct_books = set(bookset)
    bookset_subset_price = (
        len(distinct_books)
        * SINGLE_BOOK_PRICE
        * (1 - DISCOUNT_PCTS[len(distinct_books)] / 100)
    )
    return bookset_subset_price + price_of_bookset(
        tuple(
            sorted(remove_bookset_from_basket(tuple(sorted(distinct_books)), bookset))
        )
    )


if __name__ == "__main__":
    basket = [1, 1, 2, 2, 3, 3, 4, 5]
    print(total(basket))
