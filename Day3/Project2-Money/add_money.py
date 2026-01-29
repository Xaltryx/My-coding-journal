from date_time_now import date_time_now
import Database

def add_money(db, cursor, user_id):
    while True:
        try:
            money_added = float(input("Enter the amount of money you want to add: "))
            if money_added < 0:
                print("❌ Please enter a positive number.")
                continue
            break
        except ValueError:
            print("❌ Please enter a valid number.")

    # Get last balance for this user
    old_balance = Database.get_old_balance(cursor,user_id)
    new_balance = old_balance + money_added
    Database.insert_total_money(db,cursor,date_time_now,new_balance,money_added,user_id)
    print(f"✅ {money_added} EGP deposited in your account.")
    print(f"New balance: {new_balance} EGP")