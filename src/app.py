from flask import Flask, render_template, request, redirect, url_for, session
from utilities import read_organizations_from_csv, read_users_from_csv, validate_user, filter_organizations
from dotenv import load_dotenv, dotenv_values

load_dotenv()

app = Flask(__name__)
app.secret_key = dotenv_values(".env")["FLASK_SECRET"]
# Read data from CSV files
organizations = read_organizations_from_csv('data/organizations.csv')
users = read_users_from_csv('data/users.csv')

def get_organization_data_by_id(org_id):
    for org in organizations:
        if org['id'] == org_id:
            return org
    return None


@app.route('/')
def homepage():
    return render_template('home.html')

@app.route('/organizations')
def organizations_list():
    return render_template('organizations.html', organizations=organizations)

@app.route('/organization/<int:org_id>')
def organization(org_id):
    organization_data = get_organization_data_by_id(org_id)

    if organization_data:
        return render_template('organization.html', organization=organization_data)
    else:
        return "Organization not found", 404


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = validate_user(username, password, users)
        if user:
            session['username'] = user.username
            return redirect(url_for('user_page'))  # Redirect to the user page
        else:
            return "Invalid username or password", 401
    return render_template('login.html')

@app.route('/user')
def user_page():
    if 'username' not in session:
        return redirect(url_for('login'))  # Redirect to login if not logged in
    return render_template('user.html', username=session['username'])

@app.route('/user/search')
def user_search():
    if 'username' not in session:
        return redirect(url_for('login'))

    searched_tags = request.args.get('tags')
    if searched_tags: 
        # Trim whitespace 
        searched_tags = [tag.strip().lower() for tag in searched_tags.split(',')] 

        filtered_organizations = filter_organizations(organizations, searched_tags)
    else:
        filtered_organizations = []

    return render_template('user.html', organizations=filtered_organizations, username=session['username'])



@app.route('/logout')
def logout():
    session.pop('username', None)  # logging out
    return redirect(url_for('homepage'))


if __name__ == '__main__':
    app.run(debug=True)