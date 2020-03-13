from flask import Flask, request, session, flash, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from db.mongod import find

import os

db =SQLAlchemy()
app = Flask(__name__, template_folder="template")
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://manager:sVghus765@127.0.0.1:3306/tyroo'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db.init_app(app=app)

@app.route("/")
def index():
    return "Tyroo RBE is Working !"

@app.route('/home')
def home():
    if not session.get("logged_in"):
        return render_template('login.html')
    else:
        return render_template('rule.html')


@app.route('/login', methods = ['POST',"GET"])
def login():
    if request.method == "GET":
        res = find(collection='rule', query_params={})
        return render_template('rule.html',res_list=res)
    elif request.form['password'] == "password" and request.form['email']=="abc@gmail.com":
        session['logged_in'] = True
        res = find(collection='rule', query_params={})
        return render_template('rule.html',res_list=res)
    else:
        return  home()

@app.route('/add_rule', methods = ['POST'])
def add_rule():
    rule = request.form['rule']
    campaign = request.form['campaign']
    schedule = request.form['schedule']
    condition = request.form['condition']
    action = request.form['action']
    from services.rule import addrule
    resp = addrule(rule=rule,campaign=campaign,schedule=schedule,condition=condition,action=action)
    from services.mail import send_mail
    send_mail(email="abc@outlook.com",email_to="xyz@gmail.com",email_sub="Tryoo campaign test !",password="XXXXXX",name="abc",rule=rule,campaign=campaign,schedule=schedule,condition=condition,action=action)
    return redirect("/login")
if __name__ == '__main__':
    app.secret_key = os.urandom(12)
    app.run(host="0.0.0.0", port="8585")