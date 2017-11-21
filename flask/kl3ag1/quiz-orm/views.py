# -*- coding: utf-8 -*-
# quiz-orm/views.py

from flask import render_template, request, flash
from app import app


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/formularz', methods=['GET', 'POST'])
def formularz():
    if request.method == 'POST':
        print(request.form)
        imie = request.form['imie']
        nazwisko = request.form['nazwisko']
        wiek = request.form['wiek']
        flash('Imię i nazwisko: %s %s' % (imie, nazwisko), 'kom')
    dane = [imie, nazwisko, wiek]
    return render_template('formularz.html', dane=dane)
