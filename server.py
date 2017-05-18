from flask import Flask
from flask import render_template
import random
app = Flask(__name__)
@app.route('/')
def index():
	return render_template('index.html', name='Fretti', rnd=random.randint(1,100))
@app.route('/MORO')
def MORO():
	return ':D'

if __name__=='__main__':
	app.run()