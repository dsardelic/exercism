def to_rna(dna_strand):
    return "".join(
        {"G": "C", "C": "G", "T": "A", "A": "U"}[nucleotide]
        for nucleotide in dna_strand
    )
