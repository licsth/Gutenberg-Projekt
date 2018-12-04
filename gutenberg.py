import urllib
import sys

if(len(sys.argv) > 2):
    name = sys.argv[2]
else:
    name = "buch"
f = open(name+".html", "w")
f2 = open("style.css", "r")
t2 = f2.read()
f.write("<html><head></head><style>" + t2 + "</style><body>")
j = 1
base = "http://gutenberg.spiegel.de" + sys.argv[1]
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
    f.write("<h1>Kapitel " + i + "</h1>")

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
        f.write("<p>" + (t[b2:b]) + "</p>")
        f.flush()

    j+=1

f.write("</body></html>")
f.close()
