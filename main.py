from flask import Flask, render_template, request, jsonify
from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, TextAreaField, DateTimeField
from wtforms.validators import DataRequired, InputRequired, Length
from db_module import InsertData
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'lokosecretkey'
# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:loko123@localhost:3307/new_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# define the table
class dailyplan_table(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(255), nullable=False)
    title = db.Column(db.String(255), nullable=False)
    plan = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return '<title %r>' % self.title


def create_tables():
    db.create_all()
# Initialize database
#@app.before_first_request
#create_tables()

# landing page form
class DailyForm(FlaskForm):

    #username = StringField("Username: ", validators=[DataRequired()])
    date = StringField("Date: ", validators=[DataRequired()])
    title = StringField("Title: ", validators=[DataRequired()])
    daily_plan = TextAreaField("Plan for the day: ", validators=[DataRequired()])
    submit = SubmitField('Submit')

# getting dailyplan dat from database page
class DailyPlanResultForm(FlaskForm):
    date = StringField("Date: ", validators=[DataRequired()])
    submit = SubmitField('Submit')
@app.route("/dailyplan",methods=["GET", "POST"])
def daily_plan():
    form = DailyForm()
    if request.method == "POST":
        # Check if the request is JSON (e.g., from an API client like Insomnia)
        if request.is_json:
            data = request.get_json()
            date = data.get('date')
            title = data.get('title')
            dayplan = data.get('dayplan')
            #username = data.get('username')

        elif form.validate_on_submit():
            print("form was validated")
            date = form.date.data
            title = form.title.data
            dayplan = form.daily_plan.data
            #username = form.username.data
        else:
            # If form validation fails, return the form with errors
            return render_template("home_page.html", form=form)

        #entering data directly into the database
        print(date, title, dayplan)

        insert_user_data(date=date, title=title, dayplan=dayplan)

        return f"<h1> Successfull! </h1>"
    else:
        print("form failed validation")
    return render_template("home_page.html", form=form)
# using ORM strategy
def insert_user_data(date,title, dayplan):
    with app.app_context():
        userdata = dailyplan_table(date=date, title=title, plan=dayplan)
        db.session.add(userdata)
        db.session.commit()
        msg = "user data inserted into database"
        return msg

# getting daily plan from db
@app.route("/get-dayplan", methods=["GET"])
def get_dayplan():
    form = DailyPlanResultForm()
    if request.method == "POST":
        def get_user_data():
            with app.app_context():
                data = db.session.query(dailyplan_table).all()
                return data

    elif form.validate_on_submit():
        date = form.date.data
        #return f"<h1> Wrong request method </h1>"

    else:
        return render_template("get-dayplan.html", form=form)

    return render_template("get-dayplan.html", form=form)





@app.route("/success")
def success():
    # i can create a successfull html page for redirecting after posting a dailyplan
    pass

if __name__ == '__main__':
    # with app.app_context():
    #     create_tables()
    app.run(debug=True)