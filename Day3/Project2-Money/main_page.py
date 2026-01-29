from add_money import add_money

def main_page(db,cursor,user_id):
    print("\nWelcome to the main page!")
    print("Here are the tasks:")

    tasks = ["Add money",'Exit']

    while True:
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

        choice = input("Choose an option (1-2): ").strip()

        if choice == "1":
            add_money(db,cursor,user_id)  # function to add money
        elif choice == "2":
            print("Hope I have helped you!")
            print("See you soon!")
            exit()
        else:
            print("❌ Invalid choice. Please try again.")
