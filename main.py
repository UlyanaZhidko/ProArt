import pymongo
import re
import os
import hashlib
from dotenv import load_dotenv
from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)


def pass_to_hash_func(password):
    salt = os.urandom(16)
    key = hashlib.pbkdf2_hmac('sha256', f'{password}'.encode('utf-8'), salt, 100000, dklen=68)
    storage = salt + key
    print(key, salt, storage)
    return storage


def check_pass_func(storage, password):
    salt_from_storage = storage[:16]
    key_from_storage = storage[16:]
    key = hashlib.pbkdf2_hmac('sha256', f'{password}'.encode('utf-8'), salt_from_storage, 100000, dklen=68)
    if key == key_from_storage:
        return True
    else:
        return False


def db():
    load_dotenv()
    if '/' in os.getcwd():
        user = os.environ["$MONGODB_USER"]
        password = os.environ["$MONGODB_PASSWORD"]
    else:
        user = os.environ["MONGODB_USER"]
        password = os.environ["MONGODB_PASSWORD"]
    connect = f"mongodb+srv://{user}:{password}@cluster0.zuefcwj.mongodb.net/?retryWrites=true&w=majority"
    return pymongo.MongoClient(connect)


'''
function registration() {
            var username = $("#username").val(); // Кладем текст из поля "name" в переменную
            var email = $("#email").val();
            var password = $("#password").val();
            var confirm_password = $("#confirm_password").val();
            $.get("/send_message", { "name" : name, "text" : text});
        }
'''


@app.errorhandler(404)
def page_not_found(error):
    return redirect(url_for('index'))


@app.route("/index.html")
def index():
    return render_template("/index.html")


@app.route("/login.html")
def login():
    return render_template("/login.html")


@app.route("/registration.html")
def registration():
    return render_template("/registration.html")


@app.route("/catalog.html")
def catalog():
    return render_template("/catalog.html")


# @app.route("/send_message")
def send_message():
    username = "ulyaa"  # request.args["username"]
    email = "vad.podvoyskiy@gmail.com"  # request.args["email"]
    password = "password"  # request.args["password"]
    confirm_password = "password"  # request.args["confirm_password"]
    if re.search("\@", email):
        pass
    else:
        return "Email address is incorrect"
    for row in my_collection.find({}, {"_id": 1, "username": 1, "email": 1, "storage": 1}):
        if row["username"] == username:
            return "This username already exist."
        elif row["email"] == email:
            return "You already have account"
    if password != confirm_password:
        return "Passwords not match"
    key = pass_to_hash_func(password)
    mydict = {
        "username": username,
        "email": email,
        "storage": key
    }
    my_collection.insert_one(mydict)
    return "ok"


client = db()
database = client["ProArt"]
my_collection = database["Users"]
app.run(host="0.0.0.0", port=80)
