category = ['학교', '음식', '회사', '식물', '동물', '인물', '숫자', '음료', '색상', '국가', '도시', '의류', '프로그램', '사이트', '행성', '단체', '도구', '게임', '언어', '기계', '서적', '영화', '건축물']

with open('namuwiki_corpus.txt', 'r') as corpus:
    with open('loco_kb.txt', 'a') as corpus:
        for line in corpus:
            title, document = line.split('\t')

