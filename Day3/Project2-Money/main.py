import sqlite3
from create_account import create_account
from login import login_page
from main_page import main_page
import Database

def main():
    print("Welcome to your money spending tracker.")

    with sqlite3.connect("money.sqlite") as db:
        cursor = db.cursor()

        # Check if any account exists
        accounts_exist = Database.accounts_exist(cursor)

        if not accounts_exist:
            print("\nIt looks like you don't have an account here.")
            account_created = create_account(db, cursor)
            if not account_created:
                print("\n❌ No account was created. You cannot continue without an account.")
                quit()
            else:
                print("\n✅ Account created successfully! You can now continue.")

        # Login user
        data_of_user = login_page(cursor)
        print(f"\n🎉 Welcome {data_of_user[1]}! You are now logged in and ready to track your money.")
        main_page(db,cursor,data_of_user[0])

if __name__ == "__main__":
    main()