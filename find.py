#-*- coding: UTF-8 -*-
import sys
import codecs
import os

f = codecs.open("index.csv", "r", "UTF-8")
l = f.read()

if(len(sys.argv) < 2):
    print("Bitte gib einen Suchterm ein")
    sys.exit()

allowed = ["html", "md"]

format = "html"
if(len(sys.argv) > 2):
    format = sys.argv[2]

if not format in allowed:
    print("")

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

c = int(raw_input("Which title do you choose? (please enter the number, 0 for exit) "))-1
if c == -1:
    sys.exit()

#print(list[c])
os.system("python gutenberg.py " + list[c].encode("utf8") + " '" + list2[c].encode("utf8") + "' " + format)
