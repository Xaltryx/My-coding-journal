import hashlib
import getpass
import Database

def login_page(cursor):
    print("\nWelcome to the login page.")

    while True:
        name = input("Enter your name: ").strip().lower()

        # Query user by name
        data = Database.get_user_data(cursor, name)
        if data is None:
            print("❌ We can't find your name. Please try again.\n")
            continue  # ask for name again

        # Name exists, check password
        while True:
            password = getpass.getpass("Enter your password: ")
            password_hash = hashlib.sha256(password.encode()).hexdigest()

            if password_hash == data[2]:
                print("✅ Your password is correct.")
                return data  # returns full user record
            else:
                print("❌ Your password is wrong. Please try again.\n")
