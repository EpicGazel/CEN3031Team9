class Organization:
    def __init__(self, name, short_description, long_description, tags, website_link):
        self.name = name
        self.short_description = short_description
        self.long_description = long_description
        self.tags = tags
        self.website_link = website_link

    def display_organization_info(self):
        print(f"Name: {self.name}")
        print(f"Short Description: {self.short_description}")
        print(f"Long Description: {self.long_description}")
        print(f"Tags: {', '.join(self.tags)}")
        print(f"Website Link: {self.website_link}")


# Example Usage:
if __name__ == "__main__":
    # Creating an Organization instance
    organization1 = Organization(
        "Example Organization",
        "A brief overview of the organization.",
        "A more detailed description of the organization's mission and activities.",
        ["tag1", "tag2", "tag3"],
        "https://www.example.org"
    )

    # Displaying organization information
    organization1.display_organization_info()
