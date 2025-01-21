import re


def parse(markdown):
    rval = ""
    ul_in_progress = False
    for line in markdown.split("\n"):
        if ul_in_progress and not line.startswith("* "):
            rval += "</ul>"
            ul_in_progress = False
        if line.startswith("###### "):
            token = f"<h6>{line[7:]}</h6>"
        elif line.startswith("##### "):
            token = f"<h5>{line[6:]}</h5>"
        elif line.startswith("#### "):
            token = f"<h4>{line[5:]}</h4>"
        elif line.startswith("### "):
            token = f"<h3>{line[4:]}</h3>"
        elif line.startswith("## "):
            token = f"<h2>{line[3:]}</h2>"
        elif line.startswith("# "):
            token = f"<h1>{line[2:]}</h1>"
        elif line.startswith("* "):
            token = f"<li>{line[2:]}</li>"
            if not ul_in_progress:
                token = "<ul>" + token
                ul_in_progress = True
        else:
            token = f"<p>{line}</p>"
        while re.search(r"(?<=__).+?(?=__)", token):
            token = token.replace("__", "<strong>", 1)
            token = token.replace("__", "</strong>", 1)
        while re.search(r"(?<=_).+?(?=_)", token):
            token = token.replace("_", "<em>", 1)
            token = token.replace("_", "</em>", 1)
        rval += token
    if ul_in_progress:
        rval += "</ul>"
    return rval
