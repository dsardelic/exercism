from collections import Counter


def find_anagrams(word, candidates):
    return {
        candidate
        for candidate in candidates
        if candidate.lower() != word.lower()
        and Counter(candidate.lower()) == Counter(word.lower())
    }
