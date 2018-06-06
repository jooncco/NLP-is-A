from konlpy.tag import Komoran

komoran = Komoran()
with open('namuwiki_corpus.txt', 'r') as corpus, open('loco_kb.txt', 'a') as kb:
    for line in corpus:
        nouns = komoran.nouns(line)
        for item in nouns:
            kb.write(item+'\n')