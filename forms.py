from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired

class AddGoal(FlaskForm):
    goal_category = SelectField("Select a Category", choices=["Personal Goal", "Professional Goal", "Learning Goal", "Financial Goal"], validators=[DataRequired()])
    goal_name = StringField("Goal to Achieve", default="What is your goal?", validators=[DataRequired()])
    goal_steps = StringField(" Steps to Take to Accomplish Goal", default="Description of the steps you will take to achieve your goal!", validators=[DataRequired()])
    goal_completion_date = StringField("Target completion date. Ex. 12/01/24 or Year round.", default="End of year", validators=[DataRequired()])
    status = SelectField("Completion Status", choices=["⏸️ - Not Started", "⏳ - In Progress", "⚠️ - On Hold", "✅ - Complete!"], validators=[DataRequired()])
    submit = SubmitField("Save Changes")
    #delete = SubmitField("Delete")


class EditGoal(FlaskForm):
    goal_name = StringField("Goal to Achieve", default="What is your goal?", validators=[DataRequired()])
    goal_steps = StringField(" Steps to Take to Accomplish Goal", default="Description of the steps you will take to achieve your goal!", validators=[DataRequired()])
    goal_completion_date = StringField("Target completion date. Ex. 12/01/24 or Year round.", default="End of year", validators=[DataRequired()])
    status = SelectField("Completion Status", choices=["⏸️ - Not Started", "⏳ - In Progress", "⚠️ - On Hold", "✅ - Complete!", "❌ - Delete"], validators=[DataRequired()])
    submit = SubmitField("Commit Changes")