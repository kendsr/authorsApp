# Authors Application
PyQT5 GUI app for authors in sql server pubs database

## Technology
- Python 3.6.3
- PyQT5 and Qt5 Designer
- PyODBC
- LocalDB MS SSQL Server 16

## Descrption
Application presents two list boxes (QtWidgets) designed using Qt5 Designer saved (authors.ui) and compiled with pyuic5 
into a python file (authors_UI.py) for importing into main program (authors.py).

One list box contains Auhors and another contains Titles published by the selected author
(the first by default). The data is based on the contents of the pubs sample database -- authors titleauthor and 
titles tables requiring a two table join to obtain titles for an author.

