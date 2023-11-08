class Organization:
    def __init__(self, name, short_description, long_description, tags, website_link):
        self.name = name
        self.short_description = short_description
        self.long_description = long_description
        self.tags = tags
        self.website_link = website_link

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Short Description: {self.short_description}")
        print(f"Long Description: {self.long_description}")
        print(f"Tags: {', '.join(self.tags)}")
        print(f"Website Link: {self.website_link}")

    def __str__(self):
        return f"Name: {self.name}\n - Tags: {', '.join(self.tags)}\n - Website Link: {self.website_link}"

    @staticmethod
    def enter_new_organization():
        name = input("Enter the name of the organization: ").strip()
        short_description = input("Enter a short description of the organization: ").strip()
        long_description = input("Enter a detailed description of the organization: ").strip()
    
        tags_input = input("Enter tags associated with the organization (separated by commas): ").strip()
        tags = [tag.strip() for tag in tags_input.split(",")]
    
        website_link = input("Enter the website link of the organization: ").strip()

        return Organization(name, short_description, long_description, tags, website_link)

if __name__ == "__main__":
    pass
