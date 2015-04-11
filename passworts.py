#!/usr/bin/env python3

from flask import Flask,render_template, flash, redirect
#from app import app
from forms import Input
import generator
import input

app = Flask('passworts')
app.config.from_object('config')

@app.route('/', methods=['GET', 'POST'])
def home():
    form = Input()
    return render_template('index.html', title='Home', form=form)


@app.route('/result', methods=['POST'])
def result():
    form = Input()
    if form.validate_on_submit():
        random = form.random.data
        if random == False:
            pw_length = int(form.pw_length.data)
        else:
            pw_length = 1
        pw_count = int(form.pw_count.data)
        if input.check(form) == True:
            global password_ready
            password_ready = (generator.generate(pw_length, pw_count, random))
            # return redirect('/result')
            return render_template('result.html', title='Result', password_ready=password_ready)
        else:
            return redirect('/')


@app.route('/result', methods=['GET'])
def result2():
    return redirect('/')


@app.route('/cancel', methods=['GET', 'POST'])
def cancel():
    flash("The generation sould be canceled (unsure)!")
    return redirect('/')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', title='Error')

if __name__ == '__main__':
    app.run()