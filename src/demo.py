import utilities as u
from organizations import Organization
from user import User, CreditCard


def login(users):
    print("Enter your username and password:")
    username = input("Username: ")
    password = input("Password: ")

    response = u.validate_user(username, password, users)

    return response


def list_organizations(orgs):
    for i in range(1, len(orgs) + 1):
        print(f"({i}) {orgs[i - 1]}")


def filter_organizations(orgs):
    valid_tags = u.list_tags(orgs)
    valid_tags = sorted(valid_tags)
    print("Filtering organizations by tags...")
    print("Your tag options are: all, ", end="")
    for tag in valid_tags:
        print(f"{tag}, ", end="")
    print()

    user_tags = input("Please enter one or more tags separated by commas: ").split(",")
    user_tags = [tag.strip().lower() for tag in user_tags]
    print()

    # Check if the user entered valid tag(s)
    if not all(tag in valid_tags for tag in user_tags):
        print("Invalid tag(s).")
        return orgs

    filtered_organizations = u.filter_organizations(orgs, user_tags)
    if (len(filtered_organizations) == 0):
        print("No organizations match your tag(s).")
    else:
        u.short_print(filtered_organizations)

    return filtered_organizations


def select_organizations(orgs, user):
    for i in range(1, len(orgs) + 1):
        print(f"({i}) {orgs[i - 1].name}")
    choice = int(input("Which organization would you like to read more about? Please enter a number: ")) - 1
    print()

    if choice < 0 or choice > len(orgs) - 1:
        print("Invalid number.")
    else:
        orgs[choice].display_info()

    if user is not None:
        response = input("Would you like to donate? (y/n): ")
        if response.lower() == "y":
            amount = int(input("How much would you like to donate? $").strip().replace("$", ""))
            if amount > 0:
                print("Thank you for your donation!")
            else:
                print("Invalid amount.")


def main():
    organizations = u.read_organizations_from_csv("/data/organizations.csv")
    users = u.read_users_from_csv("/data/users.csv")

    print("========== Demo functionality of donation application ==========")
    userOption = 'c'
    user = None
    curr_orgs = organizations

    while userOption.lower() != "q":
        print("\nMain Menu:")
        print("What would you like to do?")
        print("(1) Login")
        print("(2) List Organizations")
        print("(3) Select Organization to read more or donate (must be logged in to donate)")
        print("(4) Filter Organizations by tag")
        print("(5) Clear Filters")
        print("(q) Quit")
        userOption = input("Enter your choice: ")
        print("\n")

        match userOption:
            case '1':
                user = login(users)
                if user is None:
                    print("Invalid username or password.")
                else:
                    print("You have successfully logged in.")
            case '2':
                list_organizations(curr_orgs)
            case '3':
                select_organizations(curr_orgs, user)
            case '4':
                curr_orgs = filter_organizations(organizations)
            case '5':
                curr_orgs = organizations
            case 'q':
                break

    print("Thank you for using the demo!")


if __name__ == "__main__":
    main()
