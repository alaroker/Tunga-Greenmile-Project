# app/admin/forms.py

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, DateTimeField, SelectField
from wtforms.validators import DataRequired


class PackageForm(FlaskForm):
    """
    Form for admin to add or edit a department
    """
    name = StringField('Name', validators=[DataRequired()])
    date_created = StringField('Date Created', validators=[DataRequired()])
    date_to_deliver = StringField('Date To Deliver', validators=[DataRequired()])
    addressed_to = StringField('Addressed To', validators=[DataRequired()])
    package_type = SelectField('Package Type', [DataRequired()],
                        choices=[('Roll Container', 'Roll Container'),
                                 ('Box', 'Box'),('Pallette','Pallette')
                                 ])
    hub = StringField('Hub', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    submit = SubmitField('Submit')

##############################################################################
##############################################################################
##############################################################################

