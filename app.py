import os
from sqlite3 import dbapi2 as sqlite3

from flask import Flask, request, g, redirect, url_for, render_template, flash, session

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/projects')
def projects():
    return render_template('placeholder.html')

@app.route('/resume')
def resume():
    return render_template('placeholder.html')