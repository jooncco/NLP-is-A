from fastText import load_model
from sklearn.metrics.pairwise import cosine_similarity

#globals
model = load_model("wiki.ko.bin")

#graph construction
brain = dict()
with open('loco_kb.txt', 'r') as kb:
    count = 0
    for line in kb:
        entity, concept, score = line.split('\t')
        if brain.__contains__(entity):
            brain[entity] = brain[entity].append(concept)
        else:
            brain[entity] = [concept]

def isA(entity, concept):
    entity_vec = model.get_word_vector(entity)

    sim, closest = -1, ''
    for key in brain:
        if key == entity:
            return brain[entity].__contains__(concept)
        key_vec = model.get_word_vector(key)
        cur_sim = cosine_similarity([entity_vec], [key_vec])
        if sim < cur_sim:
            sim = cur_sim
            closest = key
    return brain[key].__contains__(concept)

if __name__ == "__main__":
    entity = "드레스"
    concept = "의류"
    print(isA(entity, concept))