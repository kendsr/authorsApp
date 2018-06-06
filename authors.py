
from PyQt5 import QtCore, QtGui, QtWidgets
import pyodbc 
# UI designed and comppiled from Qt5 Designer
from authors_UI import Ui_Form

def connectDB():
    # Set up ODBC connection string and connect to localDB
    con = pyodbc.connect('Driver={ODBC Driver 13 for SQL Server};'
					'Server=(LocalDB)\\MSSQLLocalDB;'
					'integrated security=true;'
					'Database=pubs')
    return con

def getAuthors():
    con = connectDB()
    cursor = con.cursor()
    cursor.execute("select au_fname, au_lname from authors")
    rows = cursor.fetchall()
    for row in rows:
    	Author = f'{row.au_lname},{row.au_fname}'
    	ui.lstAuthors.addItem(Author)
    # Automatically select the first author in the list
    ui.lstAuthors.setCurrentRow(0)
	
    cursor.close()
    con.close()

def on_change(curr, prev):
    # Get titles for a given author when selected from list of authors
    # split the text value to get the author first and last name
    (lname, fname) = curr.text().split(",")
    # Clear list box of previous data
    ui.lstTitles.clear()
    # Connect to pubs database and set up cursor
    con = connectDB()
    cursor = con.cursor()
    # Get all titles matching the author
    cursor.execute("select t.title from titleauthor ta, titles t, authors a "
                    "where a.au_fname = ? and a.au_lname = ? "
                    "and a.au_id = ta.au_id and ta.title_id = t.title_id", fname, lname)                
    titles = cursor.fetchall()
    # Load up Titles list box
    if (len(titles) == 0):
        ui.lstTitles.addItem("No titles in store.")
    else :
        for title in titles:
            ui.lstTitles.addItem(title.title)
    cursor.close()
    con.close()
		
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    ui.lstAuthors.currentItemChanged.connect(on_change)
    getAuthors()
    Form.show()
    sys.exit(app.exec_())
