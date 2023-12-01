import csv
from organizations import Organization
from user import User, CreditCard


def full_print(list):
    for item in list:
        item.display_info()


def short_print(list):
    for item in list:
        print(item)


def validate_user(username, password, users):
    for user in users:
        if username == user.username and password == user.password:
            return user

    return None


def create_user(file_path, username, email, password, ccnumber, ccexpiration, cvv):
    payment = CreditCard(ccnumber, ccexpiration, cvv)
    user = User(username, email, password, payment)

    # export to CSV
    with open(file_path, 'a', newline='') as csvfile:
        fieldnames = ['Username', 'Email', 'Password', 'CCNumber', 'CCExpiration', 'CVV']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow({
            'Username': user.username,
            'Email': user.email,
            'Password': user.password,
            'CCNumber': user.payment_info.card_number,
            'CCExpiration': user.payment_info.expiration_date,
            'CVV': user.payment_info.cvv
        })

    return user

def read_users_from_csv(file_path, new_users_path = ""):
    users = []

    try:
        with open(file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)

            for row in reader:
                # Create a User instance for each row in the CSV
                user = User(
                    username=row['Username'],
                    email=row['Email'],
                    password=row['Password'],
                    payment_info=CreditCard(
                        card_number=row['CCNumber'],
                        expiration_date=row['CCExpiration'],
                        cvv=row['CVV']
                    )
                )
                users.append(user)

    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
    except Exception as e:
        print(f"Error: {e}")

    if new_users_path != "":
        try:
            with open(new_users_path, newline='', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile)

                for row in reader:
                    # Create a User instance for each row in the CSV
                    user = User(
                        username=row['Username'],
                        email=row['Email'],
                        password=row['Password'],
                        payment_info=CreditCard(
                            card_number=row['CCNumber'],
                            expiration_date=row['CCExpiration'],
                            cvv=row['CVV']
                        )
                    )
                    users.append(user)
        except Exception as e:
            print(f"Error adding newly created users: {e}")

    return users


def read_organizations_from_csv(file_path):
    organizations = []

    try:
        with open(file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)

            for row in reader:
                # Create an Organization instance for each row in the CSV
                organization = Organization(
                    name=row['Name'],
                    short_description=row['Short Description'],
                    long_description=row['Long Description'],
                    tags=row['Tags'].split(','),
                    website_link=row['Website Link']
                )
                organizations.append(organization)

    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
    except Exception as e:
        print(f"Error: {e}")

    return organizations

def filter_organizations(orgs, tags):
    if 'all' in tags:
        return orgs
    return [org for org in orgs if all(tag.lower() in map(str.lower, org.tags) for tag in tags)]

def list_tags(orgs):
    unique_tags = set(tag for org in orgs for tag in org.tags)
    return list(unique_tags)

def get_organization_data_by_id(org_id):
    for org in organizations:
        if org['id'] == org_id:
            return org
    return None

def get_organization_data_by_name(org_name):
    # make sure the organizations.csv is in the right directory
    with open('src/data/organizations.csv', mode='r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['Name'].strip().lower() == org_name.strip().lower():
                return row
    return None

if __name__ == "__main__":
    pass
