import sys
import json
import random
import string
# read input buffer
rapper = sys.argv[1]
f = open("./rap.json", "r")
rapList = json.load(f)

def censor(rap):
    badwords = "fuckshitbitchdickpenisvaginapussycuntnigganigger"
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
    theRap += "I can't find that rapper. Random rapper chosen. "
    rapper = "kendrick-lamar"

theRap += censor(random.choice(rapList["raps"][rapper]))

# print(rapList["raps"][rapper])
sys.stdout.write(theRap)
