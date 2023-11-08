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


if __name__ == "__main__":
    pass