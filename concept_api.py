import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Reference: https://concept.research.microsoft.com/help/
placeholder = "https://concept.research.microsoft.com/api/Concept/{}?instance={}&topK={}&smooth={}"

def getScoreByCross(instance, topK=30, smooth=0.0001):
    apitype = "ScoreByCross"
    url = placeholder.format(apitype, instance, topK, smooth)
    result = requests.get(url, verify=False)
    return result.json()

def getScoreByTypi(instance, topK=30, smooth=0.0001):
    apitype = "ScoreByTypi"
    url = placeholder.format(apitype, instance, topK, smooth)
    result = requests.get(url, verify=False)
    return result.json()