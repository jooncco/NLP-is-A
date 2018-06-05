import numpy as np
import heapq as hq
from fastText import load_model
from sklearn.metrics.pairwise import cosine_similarity

# globals
model = load_model("wiki.ko.bin")
category = ['학교', '음식', '회사', '식물', '동물', '인물', '숫자', '음료', '색상', '국가', '도시', '의류', '프로그램', '사이트', '행성', '단체', '도구', '게임', '언어', '기계', '서적', '영화', '건축물']
category_em = []
for word in category:
    category_em.append(model.get_word_vector(word))

def top_n(iterable, n):
    '''
    Returns top n items in descending order.
    '''
    h = []
    for item in iterable:
        hq.heappush(h, item)
    arr_sorted = [hq.heappop(h) for i in range(0, len(h))]
    return [arr_sorted[-i] for i in range(1, n+1)]

with open('namuwiki_corpus.txt', 'r') as corpus, open('loco_kb.txt', 'a') as kb:
    for line in corpus:
        correlations = [0]*23
        title, document = line.split('\t')

        # calculate correlations
        doc_words = document.split(' ')
        for word in doc_words:
            if word == '.':
                break
            word_vec = model.get_word_vector(word)
            for i in range(0, len(category)):
                correlations[i] = correlations[i] + cosine_similarity([category_em[i]], [word_vec])
        np.multiply(correlations, 1.0/len(doc_words))

        # sort and retain top n
        result = []
        for i in range(0, len(category)):
            result.append((correlations[i], category[i]))
        related = top_n(result, 5)

        # write
        for item in related:
            kb.write(title, '\t', item[1], '\t', item[0], '\n')
