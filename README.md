# Gutenberg-Projekt

Ein kleines Programm um Bücher aus dem Gutenberg-Projekt herunterzuladen

## Nutzung

#### Setup

```shell
> git clone https://github.com/licsth/Gutenberg-Projekt.git
> cd /path/to/repository/
```

##### Für PDF
pdfkit:
```
> pip install pdfkit
```

wkhtmltopdf:
```
# MacOS
> brew install Caskroom/cask/wkhtmltopdf
# Debian/Ubuntu
> apt-get install wkhtmltopdf
# Windows:
> choco install wkhtmltopdf
```

#### Bücher herunterladen

```shell
> python find.py [Schlagwort]
1. Buchtitel (Autor)
2. ...
Welcher Titel soll heruntergeladen werden? (bitte Nummer angeben, 0 zum Abbruch) [Nummer des gewünschten Buchs]
Titel wird heruntergeladen...
```

Das Buch wird in dem Ordner als html-Datei gespeichert.



#### Herunterladen als .md-Datei:
```shell
> python find.py [Schlagwort] md
1. Buchtitel (Autor)
2. ...
Welcher Titel soll heruntergeladen werden? (bitte Nummer angeben, 0 zum Abbruch) [Nummer des gewünschten Buchs]
Titel wird heruntergeladen...
```

#### Index aktualisieren
Falls ein Titel nicht gefunden wird aber sicher im Gutenberg-Projekt vorhanden ist sollte der Index aktualisiert werden, mittels
```shell
> python update.py
```

#### HTML-Style ändern
Der Style des Buchs im HTML-Format wird direkt aus style.css kopiert, kann also mittels Änderungen an dieser Datei für zukünftige Downloads angeändert werden.
