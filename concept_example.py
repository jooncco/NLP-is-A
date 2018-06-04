from concept_api import getScoreByCross

entity = "dress"
print("result for", entity)
print("------------------")

dress_result = getScoreByCross("dress", topK=10)
for key in dress_result:
    print(key, dress_result[key])