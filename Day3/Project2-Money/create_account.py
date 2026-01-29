from password import create_a_password
from date_time_now import date_time_now
import sqlite3
import Database

def create_account(db, cursor):
    while True:
        create_account_permission = input("Do you want to create an account? (1: yes, 0: no): ")

        if create_account_permission == "1":
            print("\nNow we will ask you for some information.")
            name = input("Name: ").strip().lower()
            if len(name) < 3:
                print("❌ Username must be at least 3 characters.")
                continue

            password_hash = create_a_password()

            # Get initial deposit
            while True:
                try:
                    base_money = float(input("Enter the amount of money you will deposit at first (EGP): "))
                    if base_money < 0:
                        print("❌ Please enter a positive number.")
                        continue
                    break
                except ValueError:
                    print("❌ Please enter a valid number.")

            try:
                # Insert user
                Database.add_new_user(db,cursor,name,password_hash)
                print("✅ Account created successfully.")

                # Get the user ID
                user_id = Database.get_user_data(cursor, name)[0]

                # Insert initial deposit
                Database.insert_total_money(date_time_now, base_money, 0, user_id)

                print(f"✅ {base_money} EGP deposited in {name}'s account.")
                return True

            except sqlite3.IntegrityError:
                print("❌ Username already exists. Please choose another name.")

        elif create_account_permission == "0":
            print("Account Creation Canceled.")
            return False

        else:
            print("❌ Invalid input. Please enter 1 or 0.")
