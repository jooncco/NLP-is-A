from fastText import load_model
from sklearn.metrics.pairwise import cosine_similarity

# globals
model = load_model('wiki.ko.bin')
category = ['학교', '음식', '회사', '식물', '동물', '인물', '숫자', '음료', '색상', '국가', '도시', '의류', '프로그램', '사이트', '행성', '단체', '도구', '게임', '언어', '기계', '서적', '영화', '건축물']
category_idx = dict()
for i in range(0, len(category)):
    category_idx[category[i]] = i

def initialize():
    magic_words = ''
    magic_words = magic_words+ '연세\t학교\t1\n'+'대학교\t학교\t1\n'+'고등학교\t학교\t1\n'+'초등학교\t학교\t1\n'+'서울\t학교\t1\n'+'유치원\t학교\t1\n'+'성당\t학교\t1\n'
    magic_words = magic_words + '포도\t음식\t1\n'+'햄버거\t음식\t1\n'+'국수\t음식\t1\n'+'김치\t음식\t1\n'+'콜라\t음식\t1\n'
    magic_words = magic_words + '삼성\t회사\t1\n'+'구글\t회사\t1\n'+'페이스북\t회사\t1\n'+'네이버\t회사\t1\n'+'아마존\t회사\t1\n'+'네이트\t회사\t1\n'+'트위터\t회사\t1\n'
    magic_words = magic_words + '나무\t식물\t1\n'+'장미\t식물\t1\n'+'꽃\t식물\t1\n'+'풀\t식물\t1\n'+'데이지\t식물\t1\n'+'나팔꽃\t식물\t1\n'+'라플레시아\t식물\t1\n'+'튤립\t식물\t1\n'
    magic_words = magic_words + '사자\t동물\t1\n'+'인간\t동물\t1\n'+'호랑이\t동물\t1\n'+'기린\t동물\t1\n'+'사람\t동물\t1\n'+'게\t동물\t1\n'+'토끼\t동물\t1\n'+'돼지\t동물\t1\n'
    magic_words = magic_words + '문재인\t인물\t1\n'+'범키\t인물\t1\n'+'로꼬\t인물\t1\n'+'씨엔블루\t인물\t1\n'+'에디킴\t인물\t1\n'+'마마무\t인물\t1\n'+'폴김\t인물\t1\n'+'김연아\t인물\t1\n'
    magic_words = magic_words + '1\t숫자\t1\n'+'2\t숫자\t1\n'+'3\t숫자\t1\n'+'4\t숫자\t1\n'+'5\t숫자\t1\n'+'7\t숫자\t1\n'+'열\t숫자\t1\n'+'하나\t숫자\t1\n'+'둘\t숫자\t1\n'+'셋\t숫자\t1\n'
    magic_words = magic_words + '콜라\t음료\t1\n'+'사이다\t음료\t1\n'+'쥬스\t음료\t1\n'+'커피\t음료\t1\n'+'참이슬\t음료\t1\n'+'맥주\t음료\t1\n'+'카스\t음료\t1\n'+'오렌지주스\t음료\t1\n'
    magic_words = magic_words + '하얀색\t색상\t1\n'+'검정\t색상\t1\n'+'빨강\t색상\t1\n'+'노랑\t색상\t1\n'+'초록\t색상\t1\n'+'파랑\t색상\t1\n'+'주황\t색상\t1\n'+'보라\t색상\t1\n'
    magic_words = magic_words + '대한민국\t국가\t1\n'+'미국\t국가\t1\n'+'러시아\t국가\t1\n'+'중국\t국가\t1\n'+'일본\t국가\t1\n'+'캐나다\t국가\t1\n'+'터키\t국가\t1\n'+'스위스\t국가\t1\n'+'독일\t국가\t1\n'
    magic_words = magic_words + '서울\t도시\t1\n'+'인천\t도시\t1\n'+'베를린\t도시\t1\n'+'베이징\t도시\t1\n'+'도쿄\t도시\t1\n'+'부산\t도시\t1\n'+'홍콩\t도시\t1\n'+'런던\t도시\t1\n'
    magic_words = magic_words + '드레스\t의류\t1\n'+'후드티\t의류\t1\n'+'모자\t의류\t1\n'+'티셔츠\t의류\t1\n'+'청바지\t의류\t1\n'+'모자\t의류\t1\n'+'운동화\t의류\t1\n'
    magic_words = magic_words + '게임\t프로그램\t1\n'+'백신\t프로그램\t1\n'+'윈도우\t프로그램\t1\n'+'포토샵\t프로그램\t1\n'+'크롬\t프로그램\t1\n'+'인터넷\t프로그램\t1\n'
    magic_words = magic_words + '구글\t사이트\t1\n'+'아마존\t사이트\t1\n'+'네이버\t사이트\t1\n'+'페이스북\t사이트\t1\n'+'다음\t사이트\t1\n'+'네이트\t사이트\t1\n'+'옥션\t사이트\t1\n'
    magic_words = magic_words + '지구\t행성\t1\n'+'토성\t행성\t1\n'+'금성\t행성\t1\n'+'화성\t행성\t1\n'+'목성\t행성\t1\n'+'수성\t행성\t1\n'+'토성\t행성\t1\n'+'천왕성\t행성\t1\n'+'해왕성\t행성\t1\n'
    magic_words = magic_words + '국경없는의사회\t단체\t1\n'+'녹십자\t단체\t1\n'+'적십자\t단체\t1\n'+'유엔\t단체\t1\n'+'동아리\t단체\t1\n'+'노동자연대\t단체\t1\n'+'팀\t단체\t1\n'
    magic_words = magic_words + '가위\t도구\t1\n'+'컴퓨터\t도구\t1\n'+'연필\t도구\t1\n'+'펜\t도구\t1\n'+'라디오\t도구\t1\n'+'빨대\t도구\t1\n'+'컵\t도구\t1\n'+'계산기\t도구\t1\n'
    magic_words = magic_words + '디아블로\t게임\t1\n'+'오버워치\t게임\t1\n'+'롤\t게임\t1\n'+'배틀그라운드\t게임\t1\n'+'워크래프트\t게임\t1\n'+'포커\t게임\t1\n'+'크레이지 아케이드\t게임\t1\n'+'메이플스토리\t게임\t1\n'
    magic_words = magic_words + '한국어\t언어\t1\n'+'영어\t언어\t1\n'+'중국어\t언어\t1\n'+'라틴어\t언어\t1\n'+'스페인어\t언어\t1\n'+'라틴어\t언어\t1\n'+'러시아어\t언어\t1\n'+'프랑스어\t언어\t1\n'
    magic_words = magic_words + '엔진\t기계\t1\n'+'자동차\t기계\t1\n'+'제초기\t기계\t1\n'+'컴퓨터\t기계\t1\n'+'포크레인\t기계\t1\n'+'휴대폰\t기계\t1\n'+'트럭\t기계\t1\n'+'노트북\t기계\t1\n'
    magic_words = magic_words + '책\t서적\t1\n'+'위인전\t서적\t1\n'+'자기개발서\t서적\t1\n'+'소설\t서적\t1\n'+'시집\t서적\t1\n'+'동화책\t서적\t1\n'+'수필\t서적\t1\n'+'산문\t서적\t1\n'+'추리소설\t서적\t1\n'
    magic_words = magic_words + '공포\t영화\t1\n'+'해리포터\t영화\t1\n'+'반지의제왕\t영화\t1\n'+'타임패러독스\t영화\t1\n'+'액션\t영화\t1\n'+'호러\t영화\t1\n'+'로맨스\t영화\t1\n'+'코믹\t영화\t1\n'
    magic_words = magic_words + '롯데타워\t건축물\t1\n'+'63빌딩\t건축물\t1\n'+'청와대\t건축물\t1\n'+'백주년 기념관\t건축물\t1\n'+'경복궁\t건축물\t1\n'+'건물\t건축물\t1\n'+'빌딩\t건축물\t1\n'+'조각상\t건축물\t1\n'+'육교\t건축물\t1\n'

    with open('basis.txt', 'w') as kb:
        kb.write(magic_words)
    kb.close()

def grow(fileName, initialGrow=False):
    basis_file, output_file = 'basis.txt', 'loco_kb.txt'
    with open(fileName, 'r') as data, open(output_file, 'a') as kb:
        # copy basis on first growth.
        if initialGrow:
            with open(basis_file, 'r') as basis:
                for line in basis:
                    kb.write(line)
        # grow
        for row in data:
            word = row.strip()
            word_vec = model.get_word_vector(word)
            score_vec = [0]*23  # scores for each category.
            cur_concept = ''
            count = -1           # number of entities in one category in basis.txt
            with open(basis_file, 'r') as basis:
                for line in basis:
                    entity, concept, score = line.split('\t')
                    score = score.strip()
                    # calculate similarity between (entity, word)
                    sim = cosine_similarity([word_vec], [model.get_word_vector(entity)])[0][0]
                    score_vec[category_idx[concept]] = score_vec[category_idx[concept]] + sim*float(score)
                    if cur_concept != concept:
                        if count > 0:
                            score_vec[category_idx[cur_concept]] = score_vec[category_idx[cur_concept]] / float(count)
                        cur_concept = concept
                        count = 1
                    else:
                        count = count + 1
                score_vec[-1] = score_vec[-1]/float(count)

            for idx in range(0, len(category)):
                if score_vec[idx] > 0.3:
                    kb.write(word+'\t'+category[idx]+'\t'+str(score_vec[idx])+'\n')

initialize()
grow('test.txt', initialGrow=True)