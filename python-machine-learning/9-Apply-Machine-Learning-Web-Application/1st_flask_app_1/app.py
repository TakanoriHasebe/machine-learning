#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 25 12:18:47 2017

@author: Takanori
"""

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')

def index():
    return render_template('first_app.html')

if __name__ == '__main__':
    app.run()

