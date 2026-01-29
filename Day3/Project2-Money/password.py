import hashlib
import getpass

def create_a_password():
    while True:
        passلword = getpass.getpass("Password: ")

        if len(password) < 8:
            print("❌ Password must be at least 8 characters.")
            continue

        confirm_password = getpass.getpass("Confirm Password: ")

        if password != confirm_password:
            print("❌ Passwords do not match. Try again.\n")
            continue

        password_hash = hashlib.sha256(password.encode()).hexdigest()
        return password_hash
