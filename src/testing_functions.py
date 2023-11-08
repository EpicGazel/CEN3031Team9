from organizations import Organization
from user import User, CreditCard
import utilities as u


def import_orgs():
    # file_path = "../src/example_organizations.csv"
    file_path = "../src/organizations.csv"

    # Reading organizations from the CSV file
    organizations_list = u.read_organizations_from_csv(file_path)
    return organizations_list


def import_users():
    # file_path = "../src/example_users.csv"
    file_path = "../src/users.csv"

    # Reading users from the CSV file
    users_list = u.read_users_from_csv(file_path)
    return users_list

def test_create_and_display_org():
    # Creating an Organization instance
    organization1 = Organization(
        "Example Organization",
        "A brief overview of the organization.",
        "A more detailed description of the organization's mission and activities.",
        ["tag1", "tag2", "tag3"],
        "https://www.example.org"
    )

    # Displaying organization information
    u.full_print([organization1])


def test_import_and_display_orgs():
    orgs = import_orgs()
    # Displaying information for each organization
    u.full_print(orgs)


def test_filter_orgs():
    orgs = import_orgs()
    # Filtering organizations by tags
    print("Filtering organizations by tags...")
    print("========== Tags: all ==========")
    filtered_organizations = u.filter_organizations(orgs, ["all"])
    u.short_print(filtered_organizations)

    print("\n========== Tags: children ==========")
    filtered_organizations = u.filter_organizations(orgs, ["children"])
    u.short_print(filtered_organizations)

    print("\n========== Tags: children, church ==========")
    filtered_organizations = u.filter_organizations(orgs, ["children", "church"])
    u.short_print(filtered_organizations)


def test_create_and_display_user():
    # Creating a CreditCard instance
    credit_card = CreditCard("1234567891011121", "12/24", "123")

    # Creating a User instance with the CreditCard instance as payment information
    user1 = User("john_doe", "john.doe@example.com", "secure_password", credit_card)

    # Displaying user information, including payment information
    user1.display_info()


def test_import_and_display_users():
    users = import_users()
    # Displaying information for each organization
    u.full_print(users)


if __name__ == "__main__":
    pass
