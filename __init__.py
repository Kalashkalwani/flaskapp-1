from flask import Flask, render_template, redirect, url_for
from os import urandom
from module1 import *


app = Flask(__name__)
app.config['CSRF_ENABLED'] = True

@app.route('/')
def homepage():
    return 'Site in construction; come again soon.'

@app.route('/result/')
def result():
    return render_template('result.html')

@app.route('/rollers/')
def rollers_summary():
    return render_template('rollers.html',roller=None)

@app.route('/rollers/<int:r_id>')
def rollers(r_id):
    if r_id not in [24, 25]:
        r_id = None
    return render_template('rollers.html',roller=r_id)

@app.route('/form/', methods=['GET','POST'])
def renderForm():
    form = testForm()
    status = False
    if form.is_submitted():
        print "submitted"
    if form.validate():
        print "valid"
        status = True
    else:
        print (form.errors)

    if status:
        # status = {'status': 'SUCCESS',
        #           'answer': form.answer.data,
        #           'other': form.other.data}
        return redirect(url_for('result'))
    try: 
        return render_template('form.html', form=form)
    except Exception as e:
        return str(e)
    
if __name__ == '__main__':
    app.run(debug=True)
    #app.run(ssl_context=context)
    #app.run(host='0.0.0.0', ssl_context=context)
    
        
