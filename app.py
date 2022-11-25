from flask import Flask, render_template, request, flash, Blueprint

import pyrebase
from flask import Flask, session, render_template, request, url_for, redirect, session, send_file
from flask import get_flashed_messages, flash
import firebase_admin
from firebase_admin import credentials
from firebase_admin import credentials, firestore, storage

app = Flask(__name__)
bp = Blueprint('main_page', __name__, template_folder='templates')
app.config["SECRET_KEY"] = "bharat"
config = {
  "apiKey": "AIzaSyBBmtTafVJT-A4fxz4OlFVVcIHog_zIJnc",
  "authDomain": "sanvardhitbharat.firebaseapp.com",
  "databaseURL": "https://sanvardhitbharat-default-rtdb.firebaseio.com/",
  "projectId": "sanvardhitbharat",
  "storageBucket": "sanvardhitbharat.appspot.com",
  "messagingSenderId": "1046153406106",
  "appId": "1:1046153406106:web:46059ba423ec0fc1ebe123",
  "measurementId": "G-G3B8XQ7JT4"
}
cred = credentials.Certificate("sanvardhitbharat-firebase-adminsdk-6gnlu-08957a71e9.json")
firebase_admin.initialize_app(cred)
firebase1 = pyrebase.initialize_app(config)
auth = firebase1.auth()
@app.route('/')
def home():  # put application's code here
    return render_template('./index.html')

@app.route("/signup", methods=['post', 'get'])
def signup():
    print("message", request.form)

    message = 'Signup to your account'

    if request.method == "POST":
        try:
            name = request.form.get("name")

            email = request.form.get("email")
            password1 = request.form.get("password")
            user = auth.create_user_with_email_and_password(email, password1)
            auth.get_account_info(user['idToken'])
            return render_template("./home.html")
        except Exception as e:
            e = "Your Email already Registered"
            flash(e)
            return render_template("./index.html")


@app.route("/login", methods=["POST", "GET"])
def login():
    messages = 'Please check your Email and password'
    if('user 'in session):
        return 'Hi,{}'.format(session['user'])
    if request.method == "POST":
        try:
            email = request.form.get("email")
            password = request.form.get("password")

            user = auth.sign_in_with_email_and_password(email, password)
            auth.get_account_info(user['idToken'])
            session['user']=email

            return render_template("./home.html")
        except:
            flash(messages)
            return render_template("./index.html", message=messages)

@app.route("/service")
def service():
    return render_template("./service.html")
@app.route("/aug")
def ar():
    return render_template("./aug.html")
@app.route("/vr")
def vr():
    return render_template("./vr.html")
@app.route("/360")
def _360():
    return render_template("./360.html")
@app.route("/live")
def live():
    return render_template("./live.html")
@app.route("/viewvr")
def viewvr():
    return render_template("./viewvr.html")
@app.route("/app")
def __app():
    return render_template("./app.html")
@app.route("/app2")
def _app_2():
    return render_template("./app2.html")
@app.route("/app3")
def _app_3():
    return render_template("./app3.html")
@app.route("/gat_index")
def gateway():
    return render_template("./gat_index.html")
@app.route("/the_index")
def theatre():
    return render_template("./the_index.html")
@app.route("/vr_index1")
def vr_index():
    return render_template("./vr_index1.html")

@app.route("/logout", methods=['post', 'get'])
def logout():
    if request.method =="POST":
        auth.current_user = None
        return render_template("./index.html")
if __name__ == '__main__':
    app.run()
