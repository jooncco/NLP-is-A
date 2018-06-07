import sys
sys.path.append('/Users/jieun/PycharmProjects/untitled/AI/NLP_is-A-master/')
import isa_predict as isa

with open('isa_pair_testset.tsv', 'r') as test:
    title_flag = True
    count_total = 0
    count_correct = 0
    for line in test:
        print(line.strip())
        if title_flag:
            title_flag = False
            continue
        entity, concept = line.split('\t')
        concept = concept.strip()
        if isa.isA(entity, concept):
            count_correct = count_correct + 1
        count_total = count_total + 1
        print(count_correct, '/', count_total)

print('Overall Accuracy: ', float(count_correct)/float(count_total))


