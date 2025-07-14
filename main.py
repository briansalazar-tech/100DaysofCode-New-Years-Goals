import pandas as pd
import os
from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from forms import AddGoal, EditGoal
from dotenv import load_dotenv

load_dotenv()

# Global Variables
MAIN_TITLE = "New Years Resolutions"
MAIN_SUBTITLE = "New year, better you! Set your goals and cross them off!"
ADD_TITLE = "Add a Goal"
ADD_SUBTITLE = "Add a new goal to work towards!" 
EDIT_TITLE = "Update Your Goal"
EDIT_SUBTITLE = "Lets Make Some Changes!"
PERSONAL_GOAL_LIST = []
PROFESSIONAL_GOAL_LIST = []
LEARNING_GOAL_LIST = []
FINANCIAL_GOAL_LIST = []

# App Setup
app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get("FLASK_APP_SECRET_KEY")
bootstrap = Bootstrap5(app)

### DATABASE CREATION ###
db_uri = app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///newyearsgoals.db?charset=utf8mb4'
db = SQLAlchemy()
db.init_app(app)

# Personal table
class PersonalGoals(db.Model):
    __tablename__ = "personalgoals"
    id = db.Column(db.Integer, primary_key=True)
    goal_category = (db.String(100))
    goal_name = db.Column(db.String(100))
    goal_steps = db.Column(db.String(500))
    goal_completion_date = db.Column(db.String(100))
    status = db.Column(db.String(50))


# Professional table
class ProfessionalGoals(db.Model):
    __tablename__ = "professionalgoals"
    id = db.Column(db.Integer, primary_key=True)
    goal_category = (db.String(100))
    goal_name = db.Column(db.String(100))
    goal_steps = db.Column(db.String(500))
    goal_completion_date = db.Column(db.String(100))
    status = db.Column(db.String(50))


# Learning table
class LearningGoals(db.Model):
    __tablename__ = "learninggoals"
    id = db.Column(db.Integer, primary_key=True)
    goal_category = (db.String(100))
    goal_name = db.Column(db.String(100))
    goal_steps = db.Column(db.String(500))
    goal_completion_date = db.Column(db.String(100))
    status = db.Column(db.String(50))


# Financial Table
class FinancialGoals(db.Model):
    __tablename__ = "financialgoals"
    id = db.Column(db.Integer, primary_key=True)
    goal_category = (db.String(100))
    goal_name = db.Column(db.String(100))
    goal_steps = db.Column(db.String(500))
    goal_completion_date = db.Column(db.String(100))
    status = db.Column(db.String(50))

# Db Create
with app.app_context():
    db.create_all()


### FLASK WEB ROUTES ###
@app.route("/")
def home():
    global PERSONAL_GOAL_LIST
    global PROFESSIONAL_GOAL_LIST
    global LEARNING_GOAL_LIST
    global FINANCIAL_GOAL_LIST

    # Render Personal Goal List from Personal Table
    PERSONAL_GOAL_LIST = [["Goal", "Steps to Accomplish", "Target Completion Date", "Status", "Quick Complete"]]
    df = pd.read_sql_table("personalgoals", con='sqlite:///./instance/newyearsgoals.db')
    for index, row in df.iterrows():
        personal_df_list = [row.goal_name, row.goal_steps, row.goal_completion_date, row.status, "Mark Complete"]
        PERSONAL_GOAL_LIST.append(personal_df_list)
    
    # Render Professional Goal List from Personal Table
    PROFESSIONAL_GOAL_LIST = [["Goal", "Steps to Accomplish", "Target Completion Date", "Status", "Quick Complete"]]
    df = pd.read_sql_table("professionalgoals", con='sqlite:///./instance/newyearsgoals.db')
    for index, row in df.iterrows():
        professional_df_list = [row.goal_name, row.goal_steps, row.goal_completion_date, row.status, "Mark Complete"]
        PROFESSIONAL_GOAL_LIST.append(professional_df_list)
    
    # Render Learning Goal List from Personal Table
    LEARNING_GOAL_LIST = [["Goal", "Steps to Accomplish", "Target Completion Date", "Status", "Quick Complete"]]
    df = pd.read_sql_table("learninggoals", con='sqlite:///./instance/newyearsgoals.db')
    for index, row in df.iterrows():
        learning_df_list = [row.goal_name, row.goal_steps, row.goal_completion_date, row.status, "Mark Complete"]
        LEARNING_GOAL_LIST.append(learning_df_list)
    
    # Render Financial Goal List from Personal Table
    FINANCIAL_GOAL_LIST = [["Goal", "Steps to Accomplish", "Target Completion Date", "Status", "Quick Complete"]]
    df = pd.read_sql_table("financialgoals", con='sqlite:///./instance/newyearsgoals.db')
    for index, row in df.iterrows():
        financial_df_list = [row.goal_name, row.goal_steps, row.goal_completion_date, row.status, "Mark Complete"]
        FINANCIAL_GOAL_LIST.append(financial_df_list)

    return render_template("index.html", 
                           title=MAIN_TITLE, 
                           subtitle=MAIN_SUBTITLE, 
                           personal_goal_list=PERSONAL_GOAL_LIST, 
                           professional_goal_list=PROFESSIONAL_GOAL_LIST, 
                           learning_goal_list=LEARNING_GOAL_LIST, 
                           financial_goal_list=FINANCIAL_GOAL_LIST)


### ADD GOALS ###
@app.route("/goal", methods=["GET", "POST"])
def goal():
    goal_form = AddGoal()
    if goal_form.validate_on_submit():
        # Personal DB Table Entry
        if goal_form.goal_category.data == "Personal Goal":
            new_goal = PersonalGoals(
                goal_category = request.form.get("goal_category"),
                goal_name = request.form.get("goal_name"),
                goal_steps = request.form.get("goal_steps"),
                goal_completion_date = request.form.get("goal_completion_date"),
                status = request.form.get("status"),
            )

            db.session.add(new_goal)
            db.session.commit()

            return redirect(url_for("home"))

        # Professional DB Table Entry
        if goal_form.goal_category.data == "Professional Goal":
            new_goal = ProfessionalGoals(
                goal_category = request.form.get("goal_category"),
                goal_name = request.form.get("goal_name"),
                goal_steps = request.form.get("goal_steps"),
                goal_completion_date = request.form.get("goal_completion_date"),
                status = request.form.get("status"),
            )

            db.session.add(new_goal)
            db.session.commit()

            return redirect(url_for("home"))

        # Learning DB Table Entry
        if goal_form.goal_category.data == "Learning Goal":
            new_goal = LearningGoals(
                goal_category = request.form.get("goal_category"),
                goal_name = request.form.get("goal_name"),
                goal_steps = request.form.get("goal_steps"),
                goal_completion_date = request.form.get("goal_completion_date"),
                status = request.form.get("status"),
            )

            db.session.add(new_goal)
            db.session.commit()

            return redirect(url_for("home"))

        # Educational DB Table Entry
        if goal_form.goal_category.data == "Financial Goal":
            new_goal = FinancialGoals(
                goal_category = request.form.get("goal_category"),
                goal_name = request.form.get("goal_name"),
                goal_steps = request.form.get("goal_steps"),
                goal_completion_date = request.form.get("goal_completion_date"),
                status = request.form.get("status"),
            )

            db.session.add(new_goal)
            db.session.commit()

            return redirect(url_for("home"))
    
    return render_template("goal.html", 
                           title=ADD_TITLE, 
                           subtitle=ADD_SUBTITLE, 
                           goal_form=goal_form)


### QUICK COMPLETE ###
# Personal Entry Quick Complete
@app.route("/complete/personal")
def personal_complete():
    goal_id = int(request.args.get("id")) # Goal ID is the item row from the list.
    listed_name = PERSONAL_GOAL_LIST[goal_id][0] # Index 0 is name column in list.
    goal_result = db.session.execute(db.select(PersonalGoals).where(PersonalGoals.goal_name == listed_name)) # Select DB entry by name instead of id column. Goal_name is column in DB.
    goal = goal_result.scalar()
    goal.status = "✅ - Complete!"
    
    db.session.commit()

    return redirect(url_for("home"))


# Professional Entry Quick Complete
@app.route("/complete/professional")
def professional_complete():
    goal_id = int(request.args.get("id"))
    listed_name = PROFESSIONAL_GOAL_LIST[goal_id][0]
    goal_result = db.session.execute(db.select(ProfessionalGoals).where(ProfessionalGoals.goal_name == listed_name))
    goal = goal_result.scalar()
    goal.status = "✅ - Complete!"
    
    db.session.commit()

    return redirect(url_for("home"))


# Learning Entry Quick Complete
@app.route("/complete/learning")
def learning_complete():
    goal_id = int(request.args.get("id"))
    listed_name = LEARNING_GOAL_LIST[goal_id][0]
    goal_result = db.session.execute(db.select(LearningGoals).where(LearningGoals.goal_name == listed_name))
    goal = goal_result.scalar()
    goal.status = "✅ - Complete!"
    
    db.session.commit()

    return redirect(url_for("home"))


# Financial Entry Quick Complete
@app.route("/complete/financial")
def financial_complete():
    goal_id = int(request.args.get("id"))
    listed_name = FINANCIAL_GOAL_LIST[goal_id][0]
    goal_result = db.session.execute(db.select(FinancialGoals).where(FinancialGoals.goal_name == listed_name))
    goal = goal_result.scalar()
    goal.status = "✅ - Complete!"
    
    db.session.commit()

    return redirect(url_for("home"))


### GOAL UPDATE/DELETE ROUTES ###
# Personal Table Entry Modifications
@app.route("/edit/personal", methods=["GET", "POST"])
def personal_edit():
    goal_id = int(request.args.get("id"))
    listed_name = PERSONAL_GOAL_LIST[goal_id][0]
    goal_result = db.session.execute(db.select(PersonalGoals).where(PersonalGoals.goal_name == listed_name))
    goal = goal_result.scalar()

    edit_form = EditGoal(
        goal_name = goal.goal_name,
        goal_steps = goal.goal_steps,
        goal_completion_date = goal.goal_completion_date,
        status = goal.status,
    )

    if edit_form.validate_on_submit():
        # Delete Entry
        if edit_form.status.data == "❌ - Delete":
            db.session.delete(goal)
            db.session.commit()

            return redirect(url_for('home'))
        
        # Save Updates
        else:
            goal.goal_name = edit_form.goal_name.data
            goal.goal_steps = edit_form.goal_steps.data
            goal.goal_completion_date = edit_form.goal_completion_date.data
            goal.status = edit_form.status.data
            db.session.commit()

            return redirect(url_for("home"))

    return render_template("goal.html", 
                           goal_form=edit_form, 
                           title=EDIT_TITLE,
                           subtitle=EDIT_SUBTITLE)


# Professional Table Entry Modificaitons
@app.route("/edit/professional", methods=["GET", "POST"])
def professional_edit():
    goal_id = int(request.args.get("id"))
    listed_name = PROFESSIONAL_GOAL_LIST[goal_id][0]
    goal_result = db.session.execute(db.select(ProfessionalGoals).where(ProfessionalGoals.goal_name == listed_name))
    goal = goal_result.scalar()

    edit_form = EditGoal(
        goal_name = goal.goal_name,
        goal_steps = goal.goal_steps,
        goal_completion_date = goal.goal_completion_date,
        status = goal.status,
    )

    if edit_form.validate_on_submit():
        # Delete Entry
        if edit_form.status.data == "❌ - Delete":
            db.session.delete(goal)
            db.session.commit()

            return redirect(url_for('home'))
        
        # Save Updates
        else:
            goal.goal_name = edit_form.goal_name.data
            goal.goal_steps = edit_form.goal_steps.data
            goal.goal_completion_date = edit_form.goal_completion_date.data
            goal.status = edit_form.status.data
            db.session.commit()

            return redirect(url_for("home"))

    return render_template("goal.html", 
                           goal_form=edit_form,
                           title=EDIT_TITLE,
                           subtitle=EDIT_SUBTITLE)


# Learning Table Entry Modifications
@app.route("/edit/learning", methods=["GET", "POST"])
def learning_edit():
    goal_id = int(request.args.get("id"))
    listed_name = LEARNING_GOAL_LIST[goal_id][0]
    goal_result = db.session.execute(db.select(LearningGoals).where(LearningGoals.goal_name == listed_name))
    goal = goal_result.scalar()
    
    edit_form = EditGoal(
        goal_name = goal.goal_name,
        goal_steps = goal.goal_steps,
        goal_completion_date = goal.goal_completion_date,
        status = goal.status,
    )

    if edit_form.validate_on_submit():
        # Delete Entry
        if edit_form.status.data == "❌ - Delete":
            db.session.delete(goal)
            db.session.commit()

            return redirect(url_for('home'))
        
        # Save Updates
        else:
            goal.goal_name = edit_form.goal_name.data
            goal.goal_steps = edit_form.goal_steps.data
            goal.goal_completion_date = edit_form.goal_completion_date.data
            goal.status = edit_form.status.data
            db.session.commit()

            return redirect(url_for("home"))

    return render_template("goal.html", 
                           goal_form=edit_form,
                           title=EDIT_TITLE,
                           subtitle=EDIT_SUBTITLE)


# Financial Table Entry Modifications
@app.route("/edit/financial", methods=["GET", "POST"])
def financial_edit():
    goal_id = int(request.args.get("id"))
    listed_name = FINANCIAL_GOAL_LIST[goal_id][0]
    goal_result = db.session.execute(db.select(FinancialGoals).where(FinancialGoals.goal_name == listed_name))
    goal = goal_result.scalar()

    edit_form = EditGoal(
        goal_name = goal.goal_name,
        goal_steps = goal.goal_steps,
        goal_completion_date = goal.goal_completion_date,
        status = goal.status,
    )

    if edit_form.validate_on_submit():
        # Delete Entry
        if edit_form.status.data == "❌ - Delete":
            db.session.delete(goal)
            db.session.commit()

            return redirect(url_for('home'))
        
        # Save Updates
        else:
            goal.goal_name = edit_form.goal_name.data
            goal.goal_steps = edit_form.goal_steps.data
            goal.goal_completion_date = edit_form.goal_completion_date.data
            goal.status = edit_form.status.data
            db.session.commit()

            return redirect(url_for("home"))

    return render_template("goal.html", 
                           goal_form=edit_form,
                           title=EDIT_TITLE,
                           subtitle=EDIT_SUBTITLE)


if __name__ == "__main__":
    app.run(debug=True, port=5002)