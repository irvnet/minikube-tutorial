from flask import Flask
app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return "\n yup... got a dockerized flask app... "

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')


