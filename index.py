import urllib
import sys
import codecs

f = codecs.open("index.csv", "w", "ISO-8859-1")
s = urllib.urlopen("http://gutenberg.spiegel.de/buch")
t = s.read()
t = t.decode("ISO-8859-1")

start = t.find('div id="spTeaserColumn"')
end = t.find("</div>", start)
h3s = t[start:end].split("<h3>")
i=1
while i < len(h3s):
    if "Jaroslav" in h3s[i]:
        i+=1
        continue
    author = h3s[i][:h3s[i].find("</h3>")]
    liste = h3s[i].split("</a>")
    for li in liste:
        hrefs = li.find("href")+6
        hrefe = li.find(">", hrefs)-2
        titles = li.find('">')+2
        title = li[titles:]
        if "br/>" in title:
            continue
        if hrefs < 6 or hrefe < -1 or titles < 2:
            continue
        f.write(author + ";")
        f.write(li[titles:] + ";")
        f.write(li[hrefs:hrefe] + ";\n")
    i+=1
