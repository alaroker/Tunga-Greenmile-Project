# app/admin/forms.py

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, DateTimeField, SelectField
from wtforms.validators import DataRequired
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from ..models import Package


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


class LoaderAssignForm(FlaskForm):
    """
    Form for admin to assign departments and roles to employees
    """
    package = QuerySelectField(query_factory=lambda: Package.query.all(),
                                  get_label="name")
    # role = QuerySelectField(query_factory=lambda: Role.query.all(),
    #                         get_label="name")
    submit = SubmitField('Submit')