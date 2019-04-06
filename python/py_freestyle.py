import sys
import json
import random
import string
import re
# read input buffer
f = open("./rap.json", "r")
rapList = json.load(f)
rapper = random.choice(list(rapList["raps"].keys()))
def censor(rap):
    badwords = "motherfuck motherfucking motherfuckin' fuckin' motherfucker f*****' f*** f****** fuck shit shits bitch bitches dick penis vagina pussy cunt nigga nigger niggas niggers".split()
    rapList = rap.split();
    for i in range(rapList):
        # if [m.start() for m in re.finditer('fuck|shit|nigg|dick|penis|vagina|pussy|cunt', word)]:
        if re.search('[a-z]*(fuck|shit|nigg|dick|penis|vagina|pussy|cunt)[a-z]*', rapList[i]) is not None:
            rapList[i] = "<say-as interpret-as='expletive'>censor</say-as>"

    return " ".join(rapList)

    # rapList = rap.split()
    # while i < len(rapList):
    #     if rapList[i] in badwords:
    #         rapList[i] = "<say-as interpret-as='expletive'>censor</say-as>"
    #     i += 1
    # return " ".join(rapList)

theRap = ""
rapper = rapper.lower().replace(" ", "-")

if rapper not in rapList["raps"]:
    rapper = random.choice(list(rapList["raps"].keys()))
    # print(rapper)
    theRap += "I can't find that rapper. " + rapper + " rapper chosen. "

for i in range(0,6):
    rapper = random.choice(list(rapList["raps"].keys()))
    theRap += censor(random.choice(rapList["raps"][rapper]))

# print(rapList["raps"][rapper])
sys.stdout.write(theRap)
