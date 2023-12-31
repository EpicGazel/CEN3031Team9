from flask import Flask, render_template, request, redirect, url_for, session
from utilities import read_organizations_from_csv, read_users_from_csv, validate_user, create_user, filter_organizations, get_organization_data_by_name, get_organization_data_by_id, is_username_taken
from dotenv import load_dotenv, dotenv_values

load_dotenv()

app = Flask(__name__)
app.secret_key = dotenv_values(".env")["FLASK_SECRET"]
# Read data from CSV files
organizations = read_organizations_from_csv('./data/organizations.csv')
users = read_users_from_csv('./data/users.csv')

@app.route('/')
def homepage():
    return render_template('home.html')

@app.route('/organizations')
def organizations_list():
    return render_template('organizations.html', organizations=organizations)

@app.route('/login', methods=['GET', 'POST'])
def login():
    error_message = None
    
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        users = read_users_from_csv('./data/users.csv')
        user = validate_user(username, password, users)
        if user:
            session['username'] = user.username
            return redirect(url_for('user_page'))  # redirect to the user page
        else:
            error_message = "Invalid username or password. Please try again."
    return render_template('login.html', error=error_message)

@app.route('/user')
def user_page():
    if 'username' not in session:
        return redirect(url_for('login'))  # redirect to login
    return render_template('user.html', username=session['username'])

@app.route('/user/search')
def user_search():
    if 'username' not in session:
        return redirect(url_for('login'))

    searched_tags = request.args.get('tags')
    if searched_tags: 
        # trim 
        searched_tags = [tag.strip().lower() for tag in searched_tags.split(',')] 

        filtered_organizations = filter_organizations(organizations, searched_tags)
    else:
        filtered_organizations = []

    return render_template('user.html', organizations=filtered_organizations, username=session['username'])

@app.route('/organization/<string:org_name>')
def organization_details(org_name):
    organization_data = get_organization_data_by_name(org_name)
    if organization_data:
        return render_template('organization_details.html', organization=organization_data)
    else:
        return "Organization not found", 404

@app.route('/logout')
def logout():
    session.pop('username', None)  # logging out
    return redirect(url_for('homepage'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    error_message = None

    if request.method == 'POST':
        # extract registration data
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        ccnumber = request.form['ccnumber']
        ccexpiration = request.form['ccexpiration']
        cvv = request.form['cvv']

        users = read_users_from_csv('./data/users.csv')
        
        # Check if username is already taken
        if is_username_taken(username, users):
            error_message = "Username already taken. Please try a different username."
        else:
            # create a new user
            new_user = create_user('./data/users.csv', username, email, password, ccnumber, ccexpiration, cvv)
            return redirect(url_for('login'))

    return render_template('register.html', error=error_message)

@app.route('/customer-support')
def customer_support():
    return render_template('customer_support.html')

@app.route('/organization-form')
def organization_form():
    return render_template('organization_form.html')

@app.route('/process-donation', methods=['POST'])
def process_donation():
    donation_amount = request.form.get('donation_amount')
    # add logic to process the donation, aka record it in a database
    return render_template('thank_you.html', donation_amount=donation_amount)

@app.route('/thank-you')
def thank_you():
    donation_amount = request.args.get('donation_amount')
    return render_template('thank_you.html', donation_amount=donation_amount)

@app.route('/submit-support', methods=['POST'])
def submit_support_form():
    # process from data here if desired
    # e.g. send an email, save the data to .csv
    return redirect(url_for('confirm_form_submission'))

@app.route('/confirm-form-submission')
def confirm_form_submission():
    return render_template('confirm_form_submission.html')


if __name__ == '__main__':
    app.run(debug=True)