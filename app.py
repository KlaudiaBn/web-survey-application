from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'mandk.mysql.pythonanywhere-services.com'
app.config['MYSQL_USER'] = 'mandk'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'mandk$flaskapp'

mysql = MySQL(app)


@app.route('/')
def index():
    return render_template("home.html")


@app.route("/submit", methods=['POST', 'GET'])
def submit():
    if request.method == 'POST':
        wiek = request.form['wiek']
        plec = request.form['plec']
        stopien = request.form['stopien']
        wydzial = request.form['wydzial']
        aktywny_tryb = request.form['aktywny_tryb']
        przyswajanie_wiedzy = request.form['przyswajanie_wiedzy']
        poziom_skupienia = request.form['poziom_skupienia']
        ocena = request.form['ocena']
        ilosc_snu = request.form['ilosc_snu']
        czas_zasypiania = request.form['czas_zasypiania']
        wybudzenie = request.form['wybudzenie']
        godziny_zasypiania = request.form['godziny_zasypiania']
        godziny_wstawania = request.form['godziny_wstawania']
        drzemka = request.form['drzemka']
        jakosc_snu = request.form['jakosc_snu']
        poziom_wyspania = request.form['poziom_wyspania']
        sennosc = request.form['sennosc']
        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO users VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
            id, wiek, plec, stopien, wydzial, aktywny_tryb, przyswajanie_wiedzy, poziom_skupienia, ocena, ilosc_snu,
            czas_zasypiania,
            wybudzenie, godziny_zasypiania, godziny_wstawania, drzemka, jakosc_snu, poziom_wyspania, sennosc))
        mysql.connection.commit()
        cursor.close()
        return render_template('submit.html')


@app.route("/users", methods=['POST', 'GET'])
def users():
    cursor = mysql.connection.cursor()
    wynik = cursor.execute("SELECT * FROM users")
    if wynik > 0:
        us_det = cursor.fetchall()
        return render_template('users.html', us_det=us_det)


@app.route("/wyniki", methods=['POST', 'GET'])
def result():
    return render_template('result.html')


if __name__ == '__main__':
    app.run()
