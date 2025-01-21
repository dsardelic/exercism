import itertools

SINGLE_BOOK_PRICE = 800
DISCOUNT_PCTS = (0, 0, 5, 10, 20, 25)

distinct_books = set(range(1, 6))

booksets = {
    1: tuple(itertools.combinations(distinct_books, 1)),
    2: tuple(itertools.combinations(distinct_books, 2)),
    3: tuple(itertools.combinations(distinct_books, 3)),
    4: tuple(itertools.combinations(distinct_books, 4)),
    5: tuple(itertools.combinations(distinct_books, 5)),
}

bookset_prices = {
    bookset_size: (
        bookset_size * SINGLE_BOOK_PRICE * (1 - DISCOUNT_PCTS[bookset_size] / 100)
    )
    for bookset_size in booksets
}


def total(basket):
    if not basket:
        return 0.0

    min_price = float("inf")

    def slozi_neki_od_kompleta(komplet_size, basket, curr_price):
        nonlocal min_price
        if komplet_size <= len(basket):
            for komplet in booksets.get(komplet_size, []):
                try:
                    preostala_basket = izuzmi_komplet_iz_kosare(komplet, basket)
                except ValueError:
                    pass
                else:
                    new_price = curr_price + bookset_prices[len(komplet)]
                    if not preostala_basket:
                        min_price = min(min_price, new_price)
                    else:
                        slozi_neki_od_kompleta(
                            min(komplet_size, len(preostala_basket)),
                            preostala_basket,
                            new_price,
                        )
        if komplet_size > 1:
            slozi_neki_od_kompleta(komplet_size - 1, basket, curr_price)

    slozi_neki_od_kompleta(max(key for key in booksets), basket, 0.0)
    return min_price


def izuzmi_komplet_iz_kosare(komplet, basket):
    new_basket = list(basket)
    for book in komplet:
        new_basket.remove(book)
    return new_basket


if __name__ == "__main__":
    kosara = [1]
    print(total(kosara))
