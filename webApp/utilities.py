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


def read_users_from_csv(file_path):
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



def filter_organizations(orgs, tags_search):
    # Convert search terms to a list if not already
    if not isinstance(tags_search, list):
        tags_search = [tags_search]

    # Normalize the search terms to lower case and strip any extra whitespace.
    search_terms = [term.lower().strip() for term in tags_search]
    filtered_orgs = []

    for org in orgs:
        # Normalize each tag to lower case.
        org_tags = [tag.lower().strip() for tag in org.tags]
        # Check if any search term is in the organization's tags
        if any(term in org_tags for term in search_terms):
            filtered_orgs.append(org)

    return filtered_orgs




def list_tags(orgs):
    unique_tags = set(tag for org in orgs for tag in org.tags)
    return list(unique_tags)


if __name__ == "__main__":
    pass