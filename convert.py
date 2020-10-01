import pdfkit
import sys
import os

pdfkit.from_url(sys.argv[1] + '.html', sys.argv[1] + '.pdf')
os.remove(sys.argv[1] + '.html')
