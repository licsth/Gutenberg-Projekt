import sys
import codecs

f = codecs.open("index.csv", "r", "ISO-8859-1")
l = f.read()

if(len(sys.argv) < 2):
    print("Bitte gib einen Suchterm ein")
    sys.exit()

search = sys.argv[1].lower()
a = l.split(";")

i = 1
while i < len(a):
    #print(a[i].lower())
    if search in a[i].lower():
        print(a[i] + " (" + a[i-1][1:] + ")")
    i += 3
# if not search in a:
#     print("Suchterm nicht gefunden")
#     sys.exit()

#index = a.index(search)
