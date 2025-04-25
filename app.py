#! /usr/bin/env python3
########################################################
# Simple Flask App
# Name : Sean Rokah
# Date : 2025-04-25
# Description : A simple Flask app to display a welcome message
# Version : 1.0
########################################################

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
