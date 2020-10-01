import urllib
import sys
import os

name = sys.argv[2]
format = sys.argv[3]

f2 = open("style.css", "r")
t2 = f2.read()
titleS = "## "
titleE = "\n" \
+"\n"
paragraphS = ""
paragraphE = "\n" \
+"\n"
if format == "html" or format=="pdf":
    f = open(name+".html", "w")
    f.write("<html><head><title>"+name+"</title></head><meta charset='UTF-8'/><style>" + t2 + "</style><body><h1>"+name+"</h1>")
    titleS = "<h2 id='kapitel"
    titleE = "</h2>"
    paragraphS = "<p>"
    paragraphE = "</p>"
else:
    f = open(name+".md", "w")
    f.write("# " + name + "\n")
j = 0
base = "https://www.projekt-gutenberg.org/" + sys.argv[1]
print("Titel wird heruntergeladen...")
s = urllib.urlopen(base + "/index.html")
t = s.read()

ul = t.find('ul')
ul2 = t.find("</ul>", ul)
ul = t.find("li", ul)
l = 0

titles = []
urls = []

while True:
    ul = t.find("<li>", ul+1, ul2)
    href1 = t.find("href", ul)+6
    href2 = t.find(">", href1)-1
    url = t[href1:href2]
    if "TYPE" in url:
        break
    urls.append(t[href1:href2])
    title2 = t.find("</a>", href2)
    titles.append(t[href2+2:title2])
    if ul < 0:
        break
    l += 1

if format == "html" or format == "pdf":
    f.write("<ul>")
    for i in range(l):
        f.write("<li><a href='#kapitel" + str(i+1) + "'>" + titles[i] + "</a></li>")
    f.write("</ul>")
    f.flush()


while j < l:

    if titleS == "<h2 id='kapitel":
        titleS += str(j+1)+"'>"
        f.write(titleS + titles[j] + titleE)
        titleS = "<h2 id='kapitel"
    else:
        f.write(titleS + titles[j] + titleE)

    link = base + "/" + urls[j]
    s = urllib.urlopen(link)
    t = s.read()

    b = t.find('Inhalt')
    b2 = b

    while True:
        b2 = t.find("<p>", b)+3
        if b2 < 3:
            break
        b = t.find("</p>", b+1)
        if b < 0:
            break
        f.write(paragraphS + (t[b2:b]) + paragraphE)
        f.flush()

    j+=1

if format == "html":
    f.write("</body></html>")
f.close()

if format == "pdf":
    os.system("python convert.py '" + name + "'")
