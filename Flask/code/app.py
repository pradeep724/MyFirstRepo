from flask import *

app = Flask(__name__)

## THis is context route
@app.route('/home')
def home():
    return 'This is the first Flask App'

## This is home page route
@app.route('/')
def index():
    return render_template('login.html')

## This is login page
@app.route('/login', methods=['POST','GET'])
def login():
    if request.method == 'POST':
        result = request.form
        uname = request.form['uname']
        password = request.form['pass']
        if uname == 'pradeep' and password == 'welcome':
            return 'Welcome %s' %uname
        else:
            return 'UnAuthorized'


## This is passing var to context
# @app.route('/<name>')
# def var_page(name):
#     return 'Your Input is %s' %name

## This is url redirect based on context var
@app.route('/<uri>')
def uri_redir(uri):
    if uri == 'home':
        return redirect(url_for('home'))
    if uri not in ['home','login']:
        return render_template('index.html',myname=uri)

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1')
