import itertools

PROTEIN_PER_CODON = {
    **dict.fromkeys(("AUG",), "Methionine"),
    **dict.fromkeys(("UUU", "UUC"), "Phenylalanine"),
    **dict.fromkeys(("UUA", "UUG"), "Leucine"),
    **dict.fromkeys(("UCU", "UCC", "UCA", "UCG"), "Serine"),
    **dict.fromkeys(("UAU", "UAC"), "Tyrosine"),
    **dict.fromkeys(("UGU", "UGC"), "Cysteine"),
    **dict.fromkeys(("UGG",), "Tryptophan"),
    **dict.fromkeys(("UAA", "UAG", "UGA"), "STOP"),
}

CODON_SIZE = 3


def proteins(strand):
    return [
        PROTEIN_PER_CODON[codon]
        for codon in itertools.takewhile(
            lambda codon: PROTEIN_PER_CODON[codon] != "STOP",
            [strand[i : i + CODON_SIZE] for i in range(0, len(strand), CODON_SIZE)],
        )
    ]
