import pickle
import sys

found = False

input = sys.argv[1]
# a_file = open('artists.pk', 'rb')
# artists = pickle.load(a_file)
# a_file.close()
a_file = open('artists.txt', 'r')
artists = list()
for line in a_file:
    artists.append(line[:-1])
a_file.close()

if input.lower() in artists:
    sys.stdout.write("do ")

else:
    for i in range(len(artists)):
        if input.lower() in artists[i].lower():
            sys.stdout.write("do ")
            found = True
    if not found:
        sys.stdout.write("don't ")
