from flask import *

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/addcomment')
def addcomment():
    return render_template('addcomment.html', title='Comment')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')