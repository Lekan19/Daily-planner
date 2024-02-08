from flask import Flask, render_template, request, jsonify
from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, TextAreaField, DateTimeField
from wtforms.validators import DataRequired, InputRequired, Length
from db_module import InsertData


app = Flask(__name__)
app.config['SECRET_KEY'] = 'newsecretkey'

class DailyForm(FlaskForm):

    username = StringField("Username: ", validators=[DataRequired()])
    date = StringField("Date: ", validators=[DataRequired()])
    title = StringField("Title: ", validators=[DataRequired()])
    daily_plan = TextAreaField("Plan for the day: ", validators=[DataRequired()])
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
            username = data.get('username')

        elif form.validate_on_submit():
            print("form was validated")
            date = form.date.data
            title = form.title.data
            dayplan = form.daily_plan.data
            username = form.username.data
        else:
            # If form validation fails, return the form with errors
            return render_template("home_page.html", form=form)

        user = InsertData()
        user.insert_db(date=date, username=username, title=title, dayplan=dayplan)


        return f"<h1> Successfull! </h1>"
    else:
        print("form failed validation")
    return render_template("home_page.html", form=form)

@app.route("/success")
def success():
    # i can create a successfull html page for redirecting after posting a dailyplan
    pass
#if "main" == "__name__":
if __name__ == '__main__':
    app.run(debug=True)
