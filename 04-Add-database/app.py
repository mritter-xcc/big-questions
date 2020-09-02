from flask import *
import sqlite3

DB = 'meaning-life.db'

app = Flask(__name__)
app.config['SECRET_KEY'] = '7552881e870e742c8cf590b6618a2a39'

@app.route('/')
@app.route('/home', methods=['GET', 'POST'])
def index():
    con = sqlite3.connect(DB)
    con.row_factory = sqlite3.Row
    sql = "SELECT * FROM comments"
    cur = con.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    return render_template('index.html', rows=rows)
    con.close()


@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/addcomment', methods=['GET', 'POST'])
def addcomment():
    # if get, show page
    if request.method == 'GET':
        return render_template('addcomment.html', title='Comment')
    # if post, add new comment to database
    elif request.method == 'POST':
        try:
            # collect data from add comment form
            name = request.form['name']
            title = request.form['title']
            comment = request.form['comment']
            print(name, title, comment)
            # connect to db
            con = sqlite3.connect(DB)
            # create cursor
            cur = con.cursor()
            # store query in variable
            #sql = ""
            # exectue query using variables
            cur.execute("INSERT INTO comments (name, title, comment) VALUES (?, ?, ?)", (name, title, comment))
            # commit to database
            con.commit()
            flash('Record successfully added.', 'success')
        except: # on error in above
            con.rollback()
            flash('Comment could not be added.', 'danger')
        finally:
            return redirect(url_for('index'))
            return render_template('index.html')
            con.close()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)