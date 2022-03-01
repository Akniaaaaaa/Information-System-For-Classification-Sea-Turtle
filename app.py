from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL
application = Flask(__name__)

# Mysql Connection
application.config['MYSQL_HOST'] = 'localhost'
application.config['MYSQL_USER'] = 'root'
application.config['MYSQL_PASSWORD'] = ''
application.config['MYSQL_DB'] = 'db_penyu'
mysql = MySQL(application)

# settings
application.secret_key = "mysecretkey"


@application.route('/')
def index():
    return render_template("index.html")


@application.route('/lapor', methods=['POST'])
def lapor():
    if request.method == 'POST':
        jenis_penyu = request.form['jenis_penyu']
        lokasi = request.form['lokasi']
        kondisi = request.form['kondisi']
        jenis_temuan = request.form['jenis_temuan']
        keterangan = request.form['keterangan']
        cur = mysql.connection.cursor()
        cur.execute(
            "INSERT INTO lapor (jenis_penyu, lokasi, kondisi, jenis_temuan, keterangan) VALUES (%s,%s,%s,%s,%s)", (jenis_penyu, lokasi, kondisi, jenis_temuan, keterangan))
        mysql.connection.commit()
        flash('Data Laporan Berhasil di masukan')
        return render_template("lapor.html")


@application.route('/lapor')
def laporku():
    return render_template("lapor.html")


@application.route('/deteksi')
def deteksiku():
    return render_template("deteksi.html")


if __name__ == '__main__':
    application.run(debug=True)
