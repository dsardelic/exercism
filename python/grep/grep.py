import re


def grep(pattern, flags, files):
    regex_matching_function = re.fullmatch if "-x" in flags else re.search
    regex = re.compile(pattern, flags=re.IGNORECASE if "-i" in flags else 0)
    results = []
    for file in files:
        with open(file, "rt", encoding="utf-8") as ifile:
            file_lines = ifile.read().rstrip("\n").split("\n")
        for line_number, line in enumerate(file_lines, 1):
            if bool(regex_matching_function(regex, line)) != ("-v" in flags):
                if "-l" in flags:
                    results.append(f"{file}")
                    break
                results.append(
                    f"{(file + ':') if len(files) > 1 else ''}"
                    f"{(str(line_number) + ':') if '-n' in flags else ''}"
                    f"{line}"
                )
    return ("\n".join(results) + "\n") if results else ""
