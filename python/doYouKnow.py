import sys

found = False
dbg = ""
input = sys.argv[1]
a_file = open('artists.txt', 'r')
dbg+="God damn it. 4"
artists = list()
dbg+="God damn it.3 "
for line in a_file:
    dbg+="God damn it. 2"
    artists.append(line[:-1])
dbg+="God damn it.1 "
a_file.close()
sys.stdout.write(""+dbg)
# if input.lower() in artists:
#     sys.stdout.write("do ")
#
# else:
#     for i in range(len(artists)):
#         if input.lower() in artists[i].lower():
#             sys.stdout.write("do ")
#             found = True
#     if not found:
#         sys.stdout.write("don't ")
