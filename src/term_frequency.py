import os
import re
import ru_core_news_md
import math

from collections import defaultdict

nlp = ru_core_news_md.load()

page_tokens = defaultdict(dict)
page_lemmas = defaultdict(dict)

total_count_tokens = defaultdict(int)
total_count_lemmas = defaultdict(int)
for file in os.listdir('pages'):
    page = open("pages/" + file).read()
    for word in re.findall("[А-Яа-я]+", page):
        if len(word) > 5:
            total_count_tokens[word] += 1

            lemma = nlp(word)[0].lemma_
            total_count_lemmas[lemma] += 1

            if page_tokens[file].get(word):
                page_tokens[file][word] += 1
            else:
                page_tokens[file][word] = 1

            if page_lemmas[file].get(lemma):
                page_lemmas[file][lemma] += 1
            else:
                page_lemmas[file][lemma] = 1

for page_filename in page_tokens:
    name = page_filename.split(".")[0]
    with open(f"tf-idf/token/tf-idf_{name}.txt", 'w', encoding='utf-8') as file:
        for token in page_tokens[page_filename]:
            tf = page_tokens[page_filename][token] / len(page_tokens[page_filename])
            idf = math.log10(len(total_count_tokens) / total_count_tokens[token])
            file.write(f"{token} {idf} {tf * idf}\n")

    with open(f"tf-idf/lemma/tf-idf_{name}.txt", 'w', encoding='utf-8') as file:
        for lemma in page_lemmas[page_filename]:
            tf = page_lemmas[page_filename][lemma] / len(page_lemmas[page_filename])
            idf = math.log10(len(total_count_lemmas) / total_count_lemmas[lemma])
            file.write(f"{lemma} {idf} {tf * idf}\n")
