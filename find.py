#-*- coding: UTF-8 -*-
import sys
import codecs
import os

f = codecs.open("index.csv", "r", "UTF-8")
l = f.read()

if(len(sys.argv) < 2):
    print("Usage: python find.py <title> [format]\n\twhere format is either html, pdf or md")
    sys.exit()

allowed = ["html", "md", "pdf"]

format = "html"
if(len(sys.argv) > 2):
    format = sys.argv[2]

if not format in allowed:
    print("Usage: python find.py <title> [format]\n\twhere format is either html, pdf or md")
    sys.exit()

search = sys.argv[1].lower()
a = l.split(";")

list = []
list2 = []

i = 1
j = 1
while i < len(a):
    #print(a[i].lower())
    if search in a[i].lower():
        print(str(j) + ": " + a[i] + " (" + a[i-1][1:] + ")")
        list.append(a[i+1])
        list2.append(a[i] + " (" + a[i-1][1:] + ")")
        j+=1
    i += 3

i = 0
while i < len(a):
    #print(a[i].lower())
    if search in a[i].lower():
        print(str(j) + ": " + a[i+1] + " (" + a[i][1:] + ")")
        list.append(a[i+2])
        list2.append(a[i+1] + " (" + a[i][1:] + ")")
        j+=1
    i += 3

if j == 1:
    print("Suchterm nicht gefunden")
    sys.exit()

c = int(raw_input("Welcher Titel soll heruntergeladen werden? (bitte Nummer angeben, 0 zum Abbruch) "))-1
if c == -1:
    sys.exit()

#print(list[c])
os.system("python gutenberg.py " + list[c].encode("utf8") + " '" + list2[c].encode("utf8") + "' " + format)
