from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Home Page route
@app.route("/")
def home():
    return render_template("home.html")

# Route to form used to add a new student to the database
@app.route("/enternew")
def enternew():
    return render_template("student.html")

# Route to add a new record (INSERT) student data to the database
@app.route("/addrec", methods=['POST', 'GET'])
def addrec():
    if request.method == 'POST':
        try:
            nm = request.form['nm']
            addr = request.form['add']
            city = request.form['city']
            zip = request.form['zip']

            with sqlite3.connect('database.db') as con:
                cur = con.cursor()
                cur.execute("INSERT INTO students (name, addr, city, zip) VALUES (?,?,?,?)",(nm, addr, city, zip))
                con.commit()
                msg = "Record successfully added to database"
        except sqlite3.Error as e:
            con.rollback()
            msg = "Error in the INSERT: " + str(e)
        finally:
            con.close()
            return render_template('result.html', msg=msg)
    return redirect(url_for('enternew'))

# Route to SELECT all data from the database and display in a table      
@app.route('/list')
def list():
    con = sqlite3.connect("database.db")
    con.row_factory = sqlite3.Row

    cur = con.cursor()
    cur.execute("SELECT rowid, * FROM students")

    rows = cur.fetchall()
    con.close()
    return render_template("list.html", rows=rows)

# Route that will SELECT a specific row in the database then load an Edit form 
@app.route("/edit", methods=['POST','GET'])
def edit():
    if request.method == 'POST':
        try:
            id = request.form['id']
            con = sqlite3.connect("database.db")
            con.row_factory = sqlite3.Row

            cur = con.cursor()
            cur.execute("SELECT rowid, * FROM students WHERE rowid = ?", (id,))

            rows = cur.fetchall()
        except sqlite3.Error as e:
            id=None
            rows = []
            print("Error: ", e)
        finally:
            con.close()
            return render_template("edit.html", rows=rows)
    return redirect(url_for('list'))

# Route used to execute the UPDATE statement on a specific record in the database
@app.route("/editrec", methods=['POST','GET'])
def editrec():
    if request.method == 'POST':
        try:
            rowid = request.form['rowid']
            nm = request.form['nm']
            addr = request.form['add']
            city = request.form['city']
            zip = request.form['zip']

            with sqlite3.connect('database.db') as con:
                cur = con.cursor()
                cur.execute("UPDATE students SET name=?, addr=?, city=?, zip=? WHERE rowid=?", (nm, addr, city, zip, rowid))
                con.commit()
                msg = "Record successfully edited in the database"
        except sqlite3.Error as e:
            con.rollback()
            msg = "Error in the Edit: " + str(e)
        finally:
            con.close()
            return render_template('result.html', msg=msg)
    return redirect(url_for('list'))

# Route used to DELETE a specific record in the database    
@app.route("/delete", methods=['POST','GET'])
def delete():
    if request.method == 'POST':
        try:
            rowid = request.form['id']
            with sqlite3.connect('database.db') as con:
                cur = con.cursor()
                cur.execute("DELETE FROM students WHERE rowid=?", (rowid,))
                con.commit()
                msg = "Record successfully deleted from the database"
        except sqlite3.Error as e:
            con.rollback()
            msg = "Error in the DELETE: " + str(e)
        finally:
            con.close()
            return render_template('result.html', msg=msg)
    return redirect(url_for('list'))

if __name__ == "__main__":
    app.run(debug=True)