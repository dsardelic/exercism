import re
from enum import Flag, auto


class GrepFlags(Flag):
    PREPEND_LINE_NUMBER = auto()
    OUTPUT_FILE_NAMES_ONLY = auto()
    CASE_INSENSITIVE = auto()
    INVERTED_MATCHING = auto()
    MATCH_ENTIRE_LINE = auto()


def grep(pattern, flags, files):
    grep_flags = GrepFlags(0)
    for flag in flags.split():
        match flag:
            case "-n":
                grep_flags |= GrepFlags.PREPEND_LINE_NUMBER
            case "-l":
                grep_flags |= GrepFlags.OUTPUT_FILE_NAMES_ONLY
            case "-i":
                grep_flags |= GrepFlags.CASE_INSENSITIVE
            case "-v":
                grep_flags |= GrepFlags.INVERTED_MATCHING
            case "-x":
                grep_flags |= GrepFlags.MATCH_ENTIRE_LINE

    regex_matching_function = (
        re.fullmatch if GrepFlags.MATCH_ENTIRE_LINE in grep_flags else re.search
    )
    regex = re.compile(
        pattern,
        flags=re.IGNORECASE if GrepFlags.CASE_INSENSITIVE in grep_flags else 0,
    )

    results = []
    for file in files:
        with open(file, "rt", encoding="utf-8") as ifile:
            file_lines = ifile.read().rstrip("\n").split("\n")
        for line_number, line in enumerate(file_lines, 1):
            if bool(regex_matching_function(regex, line)) != (
                GrepFlags.INVERTED_MATCHING in grep_flags
            ):
                if GrepFlags.OUTPUT_FILE_NAMES_ONLY in grep_flags:
                    results.append(f"{file}")
                    break
                results.append(
                    f"{(file + ':') if len(files) > 1 else ''}"
                    f"{(str(line_number) + ':') if GrepFlags.PREPEND_LINE_NUMBER in grep_flags else ''}"
                    f"{line}"
                )
    return ("\n".join(results) + "\n") if results else ""
