import csv
from organizations import Organization


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


# Example Usage:
if __name__ == "__main__":
    #file_path = "../data/example_organizations.csv"
    file_path = "../data/organizations.csv"

    # Reading organizations from the CSV file
    organizations_list = read_organizations_from_csv(file_path)

    # Displaying information for each organization
    for org in organizations_list:
        org.display_organization_info()
