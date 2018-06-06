with open('loco_kb.txt', 'r') as kb:
    for line in kb:
        entity, concept, score = line.split(' ')
        score = score.strip()
        print(score)