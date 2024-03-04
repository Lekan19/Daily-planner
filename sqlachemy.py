from main import app, db, dailyplan_table

user1 = dailyplan_table(date="Feb 11th", title="az104", plan="study")
# Use the application context to perform database operations
# with app.app_context():
#     db.session.add(user1)
#     db.session.commit()
#     print(user1.title)

def insert_user_data(date,title, dayplan):
    with app.app_context():
        userdata = dailyplan_table(date=date, title=title, plan=dayplan)
        db.session.add(userdata)
        db.session.commit()
        return f"ENter user data into database"

def get_user_data():
    with app.app_context():
        try:
            data = db.session.query(dailyplan_table).all()
            return data
        except Exception as e:
            print(f"Error fetching data: {e}")
            return []

#date = "03"
#itle = "savill"
get_user_data()


#insert_user_data(date="Feb 25th", title="savill", dayplan="az104 study")

# with app.app_context():
#     user2 = dailyplan_table(date="Geb 25th", title="az104", plan="cram")
#     db.session.add(user2)
#     db.session.commit()

# with app.app_context():
#     db.session.get()
# with app.app_context():
#     list = dailyplan_table.query.all()
    #print(list[0])
# db.session.add(user1)
# db.session.commit()
# print(user1.title)