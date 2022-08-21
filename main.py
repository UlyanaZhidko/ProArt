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


@app.route("/send_reg_credentials")
def send_reg_credentials():
    username = request.args["username"]
    email = request.args["email"]
    password = request.args["password"]
    second_password = request.args["second_password"]
    if re.search("\@", email):
        pass
    else:
        print("Email address is incorrect")
        return "Email address is incorrect"
    for row in my_collection.find({}, {"_id": 1, "username": 1, "email": 1, "storage": 1}):
        if row["username"] == username:
            print("This username already exist.")
            return "This username already exist."
        elif row["email"] == email:
            print("You already have account")
            return "You already have account"
    if password != second_password:
        print("Passwords not match")
        return "Passwords not match"
    key = pass_to_hash_func(password)
    mydict = {
        "username": username,
        "email": email,
        "storage": key
    }
    my_collection.insert_one(mydict)
    return redirect(url_for('index'))


client = db()
database = client["ProArt"]
my_collection = database["Users"]
app.run(host="0.0.0.0", port=80)
