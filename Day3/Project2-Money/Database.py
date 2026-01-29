def accounts_exist(cursor):
    return cursor.execute("SELECT COUNT(*) FROM personal_information").fetchone()[0] > 0

def get_old_balance(cursor,user_id):
    return cursor.execute(
        "SELECT total_money_egp FROM total_money WHERE user_id = ? ORDER BY date_time DESC LIMIT 1",
        (user_id,)).fetchone()[0]

def insert_total_money(db,cursor,date_time_now,new_balance,change,user_id):
    cursor.execute(
        "INSERT INTO total_money (date_time, total_money_egp, change_from_previous_egp, user_id) "
        "VALUES (?, ?, ?, ?)",
        (date_time_now, new_balance, change, user_id)
    )
    db.commit()

def add_new_user(db,cursor,name,password_hash):
    cursor.execute(
        "INSERT INTO personal_information (name, password_hash) VALUES (?, ?)",
        (name, password_hash)
    )
    db.commit()

def get_user_data(cursor,name):
    return cursor.execute(
        "SELECT * FROM personal_information WHERE name = ?",
        (name,)
    ).fetchone()