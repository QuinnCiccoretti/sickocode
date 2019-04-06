import sys
import json
import random
import string
# read input buffer
f = open("./rap.json", "r")
rapList = json.load(f)
rapper = random.choice(list(rapList["raps"].keys()))
def censor(rap):
    badwords = "motherfuck motherfucking motherfuckin' motherfucker f*****' f*** f****** fuck shit shits bitch bitches dick penis vagina pussy cunt nigga nigger niggas niggers".split()
    i = 0
    rapList = rap.split()
    while i < len(rapList):
        if rapList[i] in badwords:
            rapList[i] = "<say-as interpret-as='expletive'>censor</say-as>"
        i += 1
    return " ".join(rapList)

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
