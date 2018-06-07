from fastText import load_model
from sklearn.metrics.pairwise import cosine_similarity

model = load_model("wiki.ko.bin")
brain = dict()
with open('loco_kb_2.txt', 'r') as kb:
    for line in kb:
        entity, concept, score = line.split('\t')
        score = score.strip()
        if brain.get(entity) is not None:
            brain[entity].append(concept)
            # print(brain[entity])
        else:
            brain[entity] = [concept]
print('dictionary build done.')

def isA(entity, concept):
    entity_vec = model.get_word_vector(entity)

    sim, closest = -1, ''
    for key in brain:
        if key == entity:
            if brain.get(entity) is not None:
                return concept in brain[entity]
            else:
                return False
        key_vec = model.get_word_vector(key)
        cur_sim = cosine_similarity([entity_vec], [key_vec])
        if sim < cur_sim:
            sim = cur_sim
            closest = key
    if brain[closest] is not None:
        print(brain[closest])
        return (concept in brain[closest])
    else:
        return False

if __name__ == "__main__":
    entity = "드레"
    concept = "의류"
    print(isA(entity, concept))