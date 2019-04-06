rimport sys
import json
import random
import string
# read input buffer
rapper = sys.argv[1]
f = open("./rap.json", "r")
rapList = json.load(f)

def censor(rap):
    rapList = rap.split();
    for i in range(len(rapList)):
        # if [m.start() for m in re.finditer('fuck|shit|nigg|dick|penis|vagina|pussy|cunt', word)]:
        if re.search('.*(bitch|fuck|shit|nigg|dick|penis|vagina|pussy|cunt|f\*\*\*).*', rapList[i].lower()) is not None:
            rapList[i] = "<say-as interpret-as='expletive'>censor</say-as>"

    return " ".join(rapList)

theRap = ""
rapper = rapper.lower().replace(" ", "-")

if rapper not in rapList["raps"]:
    rapper = random.choice(list(rapList["raps"].keys()))
    # print(rapper)
    theRap += "I can't find that rapper. " + rapper + " rapper chosen. "


theRap += censor(random.choice(rapList["raps"][rapper]))

# print(rapList["raps"][rapper])
sys.stdout.write(theRap)
