from datetime import datetime

from flask import Flask , render_template , request
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
import json
from datetime import datetime
with open('config.json', 'r') as c:
    params = json.load(c)["params"]

local_server = True

app = Flask(__name__)
app.config.update(
    MAIL_SERVER = 'smtp.gmail.com',
    MAIL_PORT = '465',
    MAIL_USE_SSL = True,
    MAIL_USERNAME = params['gmail-user'],
    MAIL_PASSWORD = params['gmail-password']
)
mail = Mail(app)
if(local_server):
    app.config['SQLALCHEMY_DATABASE_URI'] = params['local_uri']
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = params['prod_uri']

db = SQLAlchemy(app)


app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/mydbb'
db = SQLAlchemy(app)


class Contact(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    phone_num = db.Column(db.String(12), nullable=False)
    msg = db.Column(db.String(120), nullable=False)
    date = db.Column(db.String(12), nullable=True)
    email = db.Column(db.String(20), nullable=False)

@app.route("/contact", methods = ['GET', 'POST'])
def contact():
    if(request.method=='POST'):
        '''Add entry to the database'''
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        message = request.form.get('message')
        entry = Contact(name=name, phone_num = phone, msg = message, date= datetime.now(),email = email )
        db.session.add(entry)
        db.session.commit()
        mail.send_message('New message from ' + name,
                          sender=email,
                          recipients=[params['gmail-user']],
                          body=message + "\n" + phone
                          )

    return render_template('contact.html' )




@app.route('/')
def hello_world():

   return render_template("/index.html" )

@app.route("/index.html")
def home():
    return render_template('index.html', params=params)
@app.route('/study.html')
def study():
   return render_template("study.html")
@app.route('/placement.html')
def placemeng():
   return render_template("/placement.html")
@app.route('/resume.html')
def resume():
   return render_template("resume.html")
@app.route('/guide.html')
def guide():
   return render_template("guide.html")

@app.route('/leetcode.html')
def solutions():
   return render_template("leetcode.html")

@app.route('/blogs.html')
def blogs():
   return render_template("blogs.html", params=params)
@app.route('/aws.html')
def aws():
   return render_template("aws.html")
@app.route('/pointer.html')
def pointer():
   return render_template("pointer.html")

@app.route('/chs.html')
def chsc():
   return render_template("chs.html")

@app.route('/cssch.html')
def css():
   return render_template("cssch.html")

@app.route('/htmlch.html')
def html():
   return render_template("htmlch.html")


@app.route('/jsch.html')
def js():
   return render_template("jsch.html")

@app.route('/pythonch.html')
def s():
   return render_template("pythonch.html")

@app.route('/quiz.html')
def quiz():
   return render_template("quiz.html")

@app.route('/htmlquiz.html')
def htmlq():
   return render_template("htmlquiz.html")

@app.route('/cssquiz.html')
def cssq():
   return render_template("cssquiz.html")


@app.route('/quizjs.html')
def jsq():
   return render_template("quizjs.html")

@app.route('/contact.html')
def q():
   return render_template("contact.html")




if __name__ == '__main__':
   app.run(debug=True)