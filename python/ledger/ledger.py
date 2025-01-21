from dataclasses import dataclass
from datetime import datetime
from itertools import chain
from operator import attrgetter


@dataclass
class LedgerEntry:
    date: datetime
    description: str
    change: int


@dataclass(unsafe_hash=True)
class HeaderTranslations:
    date: str
    description: str
    change: str


currency_symbols = {
    "USD": "$",
    "EUR": "€",
}

date_formats = {
    "en_US": "%m/%d/%Y",
    "nl_NL": "%d-%m-%Y",
}

currency_amount_notations = {
    "en_US": lambda c, a: f"({c}{abs(a):,.2f})" if a < 0 else f"{c}{a:,.2f} ",
    "nl_NL": lambda c, a: f"{c} {a:_.2f} ".replace(".", ",").replace("_", "."),
}

translations = {
    "en_US": HeaderTranslations("Date", "Description", "Change"),
    "nl_NL": HeaderTranslations("Datum", "Omschrijving", "Verandering"),
}


def create_entry(date, description, change):
    return LedgerEntry(datetime.strptime(date, "%Y-%m-%d"), description, change)


def format_entries(currency, locale, entries):
    return "\n".join(
        chain(
            (header_row(locale),),
            (
                body_row(currency, locale, entry)
                for entry in sorted(entries, key=attrgetter("change"))
            ),
        )
    )


def header_row(locale):
    return " | ".join(
        (
            f"{translations[locale].date:<10}",
            f"{translations[locale].description:<25}",
            f"{translations[locale].change:<13}",
        )
    )


def body_row(currency, locale, entry):
    return " | ".join(
        (
            f"{localized_date(locale, entry.date):<10}",
            f"{truncated_description(entry.description):<25}",
            f"{localized_currency_amount(currency, locale, entry.change / 100):>13}",
        )
    )


def localized_date(locale, date):
    return date.strftime(date_formats[locale])


def truncated_description(description):
    return description[:25] if len(description) < 25 else description[:22] + "..."


def localized_currency_amount(currency, locale, amount):
    return currency_amount_notations[locale](currency_symbols[currency], amount)
