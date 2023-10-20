class CreditCard:
    def __init__(self, card_number, expiration_date, cvv):
        self.card_number = card_number
        self.expiration_date = expiration_date
        self.cvv = cvv

    def display_info(self):
        print(f"\tCard Number: {self.card_number}")
        print(f"\tExpiration Date: {self.expiration_date}")
        print(f"\tCVV: {self.cvv}")


class User:
    def __init__(self, username, email, password, payment_info):
        self.username = username
        self.email = email
        self.password = password
        self.payment_info = payment_info

    def display_info(self):
        print(f"Username: {self.username}")
        print(f"Email: {self.email}")
        print(f"Password: {self.password}")
        print("Payment Information:")
        self.payment_info.display_info()

    def __str__(self):
        return f"Username: {self.username}\n - Email: {self.email}\n"


# Example Usage:
if __name__ == "__main__":
    # Creating a CreditCard instance
    credit_card = CreditCard("1234-5678-9101-1121", "12/24", "123")

    # Creating a User instance with the CreditCard instance as payment information
    user1 = User("john_doe", "john.doe@example.com", "secure_password", credit_card)

    # Displaying user information, including payment information
    user1.display_user_info()
