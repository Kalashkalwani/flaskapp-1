#from OpenSSL import SSL
from flask import Flask, render_template, jsonify, flash
from module1 import *

#context = SSL.Context(SSL.SSLv23_METHOD)
#context.use_privatekey_file('/etc/apache2/ssl/apache.key')
#context.use_certificate_file('/etc/apache2/ssl/apache.crt')

app = Flask(__name__)

@app.route('/')
def homepage():
    return 'Site in construction; come again soon.'

@app.route('/form/', methods=['GET','POST'])    
def renderForm():
    form = testForm()
    if form.validate_on_submit():
        status = {'status': 'SUCCESS',
                  'answer': form.answer.data,
                  'other': form.other.data}
        return render_template('result.html', data=status)
    try: 
        return render_template('form.html', form=form)
    except Exception as e:
        return str(e)
    
if __name__ == '__main__':
    app.run()
    #app.run(ssl_context=context)
    #app.run(host='0.0.0.0', ssl_context=context)
    
        
