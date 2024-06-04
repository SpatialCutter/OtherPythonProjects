from flask import Flask, render_template, request
from Database import Database

app = Flask(__name__)
window = "login"


@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")


@app.route('/', methods=['post', 'get'])
def form():
    access = False
    if request.method == 'POST':
        idstaff = FindInStaff(request.form.get('login'))
        if idstaff >= 0:
            access = CheckPassword(idstaff, request.form.get('pass'))
            if access:
                answer = GenerateSales()
                return render_template('sale.html', answer=answer)
    return render_template('index.html', err=access)


def FindInStaff(text):
    db = Database("dbBookShop")
    allstaff = db.SelectAll("Staff")
    for staff in allstaff:
        if text == ' '.join(staff[1:4]):
            return staff[0]
    return -1


def CheckPassword(idstaff, text):
    db = Database("dbBookShop")
    staff = db.SelectByID("Staff", idstaff)
    if text == staff[0][7]:
        return True
    return False


def GenerateSales():
    db = Database("dbBookShop")
    sale = db.SelectAll("SaleExtented")
    table = []
    for row in sale:
        book = db.SelectByID("Book", row[2])
        author = db.SelectByID("Author", book[0][2])
        name = "{0} - {1}".format(
            book[0][1],
            ' '.join([i for i in author[0][1:4] if i != 'NULL'])
        )
        row = "{0} {1} шт. по цене {2} руб.".format(name, row[4], row[3])
        table.append(row)
    return table


if __name__ == '__main__':
    app.run()
