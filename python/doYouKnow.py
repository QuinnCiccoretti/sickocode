import pickle
import sys

found = False

input = sys.argv[1]
a_file = open('artists.pk', 'rb')
artists = pickle.load(a_file)

if input in artists:
    sys.stdout.write("do")

else:
    for i in range(len(artists)):
        if input in artists[i].lower():
            sys.stdout.write("do")
            found = True
            break
    if not found:
        sys.stdout.write("don't")
