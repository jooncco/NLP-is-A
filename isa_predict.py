from fastText import load_model
from sklearn.metrics.pairwise import cosine_similarity

model = load_model("wiki.ko.bin")
brain = dict()
with open('loco_kb.txt', 'r') as kb:
    for line in kb:
        row = line.split('\t')
        if brain.__contains__(row[0]):
            brain[row[0]] = brain[row[0]].append(row[1])
        else:
            brain[row[0]] = [row[1]]

def isA(entity, concept):
    entity_vec = model.get_word_vector(entity)

    sim = -1
    closest = ''
    for key in brain:
        if key == entity:
            return brain[entity].__contains__(concept)
        key_vec = model.get_word_vector(key)
        i_sim = cosine_similarity([entity_vec], [key_vec])
        if sim < i_sim:
            sim = i_sim
            closest = key
    return brain[key].__contains__(concept)

if __name__ == "__main__":
    entity = "드레스"
    concept = "의류"
    print(isA(entity, concept))