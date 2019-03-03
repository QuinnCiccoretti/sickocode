import sys
import json
import random
# read input buffer
rapper = sys.argv[1]
f = open("./rap.json", "r")
rapList = json.load(f)

theRap = ""
rapper = rapper.lower().replace(" ", "-")

if rapper not in rapList["raps"]:
    theRap += "I can't find that rapper. Random rapper chosen. "
    rapper = "kendrick-lamar"

theRap += random.choice(rapList["raps"][rapper])

print(rapList["raps"][rapper])
sys.stdout.write(theRap)
