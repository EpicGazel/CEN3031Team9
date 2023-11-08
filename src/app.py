from flask import Flask, render_template, request, redirect, url_for, flash
import utilities as u
from organizations import Organization
from user import User, CreditCard
import csv

app = Flask(__name__, template_folder='../data/templates')
app.secret_key = 'your_secret_key'

users = u.read_users_from_csv("../data /users.csv")

@app.route('/', methods=['GET', 'POST'])
def index():
    error = None

    # On a POST request, process the form data
    if request.method == 'POST':
        username = request.form['Username']
        password = request.form['Password']
        
        if check_credentials(username, password):
            return render_template('organization-list.html')
        else:
            flash('Invalid credentials')
    return render_template('/login.html', error=error)


@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/forgot-password')
def forgotPassword():
    return render_template('forgot-password.html')

@app.route('/reset-password')
def resetPassword():
    return render_template('reset-password.html')

@app.route('/home')
def home():
    return render_template('organization-list.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/error')
def error():
    return render_template('error.html')

def check_credentials(username, password):
    with open('users.csv', mode='r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            # In real application, passwords would be hashed
            if row['Username'] == username and row['Password'] == password:
                return True
    return False

if __name__ == '__main__':
    app.run(port=5001)
