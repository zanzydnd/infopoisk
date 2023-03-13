import os
import re
from collections import defaultdict

import ru_core_news_md


def read_index_file() -> dict:
    result = {}
    with open("index.txt") as f:
        for line in f:
            filename, link = line.split(" - ")
            result[filename] = link

    return link


nlp = ru_core_news_md.load()

inverted_index = defaultdict(set)
for file in os.listdir('pages'):
    text = open("pages/" + file).read()
    for word in re.findall("[А-Яа-я]+", text):
        if len(word) > 5:
            doc = nlp(word)
            lemma = doc[0].lemma_
            inverted_index[lemma].add(file.split(".")[0])

with open("inverted_index.txt", "w") as w:
    for lemma in inverted_index.keys():
        w.write(lemma + f" {' '.join(inverted_index[lemma])}\n")
