#-*- coding: UTF-8 -*-
import urllib
import sys
import codecs

f = codecs.open("index.csv", "w", "UTF-8")
s = urllib.urlopen("https://www.projekt-gutenberg.org/info/texte/allworka.html")
t = s.read()
t = t.decode("UTF-8")

start = t.find('DL')
end = t.find("</DL>", start)
h3s = t[start:end].split("<DT>")
i=0
while i < len(h3s):
    h3s[i] = h3s[i].replace(";", ",")
    author = h3s[i][:h3s[i].find("</DT>")].strip().replace(u'ü', 'ue').replace(u'ä', 'ae').replace(u'ö', 'oe').replace(u'Ü', 'Ue').replace(u'Ä', 'Ae').replace(u'Ö', 'Oe').replace(u'ß', 'ss')
    if(not author[:3]=="<BR"):
        liste = h3s[i].split("</DD>")
        for li in liste:
            hrefs = li.find("HREF")+6+6
            hrefe1 = li.find(">", hrefs)-2
            hrefe2 = li[:hrefe1].rfind("/")
            titlee = li.find('</A>', hrefe1)
            title = li[hrefe1+3:titlee].strip().replace(u'ü', 'ue').replace(u'ä', 'ae').replace(u'ö', 'oe').replace(u'Ü', 'Ue').replace(u'Ä', 'Ae').replace(u'Ö', 'Oe').replace(u'ß', 'ss')
            href = li[hrefs:hrefe2].strip()
            if(title == "" or href == "") :
                continue
            f.write(author + ";")
            f.write(title + ";")
            f.write(href + ";\n")
            f.flush()
    i+=1
