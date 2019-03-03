import sys

found = False
input = sys.argv[1]

a_file = open("./python/artists.pk", "rb")
# artists = list()
artists = pickle.load(a_file)
# sys.stdout.write("do ")
# for line in a_file:
    # artists.append(line[:-1])
a_file.close()

if input.lower() in artists:
    sys.stdout.write("do ")

else:
    for i in range(len(artists)):
        if input.lower().replace(' ', '-') in artists[i].lower():
            sys.stdout.write("do ")
            found = True
    if not found:
        sys.stdout.write("don't ")
