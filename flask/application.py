#for debug
from __future__ import print_function # In python 2.7
import sys

from flask import Flask, render_template, request
from data import roles
from user_input_parser import get_drug


Roles = roles()
app = Flask(__name__)

@app.route('/')
@app.route('/index.html')
def index():
	return render_template('index.html')

@app.route('/result', methods=["POST", "GET"])
@app.route('/result.html', methods=["POST", "GET"])
def result():
	Drug = request.form["symptom"]
	drugs = get_drug(Drug)
	return render_template('result.html', drug = drugs)
	
@app.route('/about')
@app.route('/about.html')
def about():
	return render_template('about.html')

@app.route('/team')
@app.route('/team.html')
def team():
	return render_template('team.html', roles = Roles)

if __name__ == "__main__":
  app.run(debug=True)