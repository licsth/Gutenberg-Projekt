import urllib
import sys

name = sys.argv[2]
format = sys.argv[3]

f2 = open("style.css", "r")
t2 = f2.read()
titleS = "##"
titleE = "\n" \
+"\n"
paragraphS = ""
paragraphE = "\n" \
+"\n"
if format == "html":
    f = open(name+".html", "w")
    f.write("<html><head></head><style>" + t2 + "</style><body>")
    titleS = "<h1 id='kapitel"
    titleE = "</h1>"
    paragraphS = "<p>"
    paragraphE = "</p>"
else:
    f = open(name+".md", "w")
j = 1
base = "http://gutenberg.spiegel.de" + sys.argv[1]
print("Titel wird heruntergeladen...")
s = urllib.urlopen(base + "1")
t = s.read()

ul = t.find('ul class="gbnav"')
ul2 = t.find("</ul>", ul)
l = 0

while True:
    ul = t.find("<li>", ul+1, ul2)
    if ul < 0:
        break
    l += 1

while j < l+1:

    i = str(j)
    if titleS == "<h1 id='kapitel":
        titleS += i+"'>"
        f.write(titleS + "Kapitel " + i + titleE)
        titleS = "<h1 id='kapitel"
    else:
        f.write(titleS + "Kapitel " + i + titleE)

    link = base + i
    s = urllib.urlopen(link)
    t = s.read()

    b = t.find('Quellenangabe')
    b2 = b

    while True:
        b2 = t.find("<p>", b, len(t)-1)+3
        if b2 < 3:
            break
        b = t.find("</p>", b+1, len(t)-1)
        if b < 0:
            break
        f.write(paragraphS + (t[b2:b]) + paragraphE)
        f.flush()

    j+=1

if format == "html":
    f.write("</body></html>")
f.close()
