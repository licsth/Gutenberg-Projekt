import urllib
import sys
import codecs

f = codecs.open("index.csv", "w", "ISO-8859-1")
s = urllib.urlopen("https://www.projekt-gutenberg.org/info/texte/allworka.html")
t = s.read()
t = t.decode("ISO-8859-1")

start = t.find('dl')
end = t.find("</dl>", start)
h3s = t[start:end].split("<dt>")
i=0
while i < len(h3s):
    h3s[i] = h3s[i].replace(";", ",")
    author = h3s[i][:h3s[i].find("</dt>")].strip()
    if(not author[:3]=="<br"):
        liste = h3s[i].split("</dd>")
        for li in liste:
            hrefs = li.find("href")+6+6
            hrefe1 = li.find(">", hrefs)-2
            hrefe2 = li[:hrefe1].rfind("/")
            titlee = li.find('</a>', hrefe1)
            title = li[hrefe1+3:titlee].strip()
            href = li[hrefs:hrefe2].strip()
            if(title == "" or href == "") :
                continue
            f.write(author + ";")
            f.write(title + ";")
            f.write(href + ";\n")
            f.flush()
    i+=1
