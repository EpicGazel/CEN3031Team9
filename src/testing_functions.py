from organizations import Organization
import utilities as u


def full_print(orgs):
    for org in orgs:
        org.display_organization_info()


def short_print(orgs):
    for org in orgs:
        print(org)


def import_orgs():
    # file_path = "../data/example_organizations.csv"
    file_path = "../data/organizations.csv"

    # Reading organizations from the CSV file
    organizations_list = u.read_organizations_from_csv(file_path)
    return organizations_list


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
    full_print([organization1])


def test_import_and_display_orgs():
    orgs = import_orgs()
    # Displaying information for each organization
    full_print(orgs)


def test_filter_orgs():
    orgs = import_orgs()
    # Filtering organizations by tags
    print("Filtering organizations by tags...")
    print("========== Tags: all ==========")
    filtered_organizations = u.filter_organizations(orgs, ["all"])
    for org in filtered_organizations:
        print(org)

    print("\n========== Tags: children ==========")
    filtered_organizations = u.filter_organizations(orgs, ["children"])
    for org in filtered_organizations:
        print(org)

    print("\n========== Tags: children, church ==========")
    filtered_organizations = u.filter_organizations(orgs, ["children", "church"])
    for org in filtered_organizations:
        print(org)


if __name__ == "__main__":
    pass
