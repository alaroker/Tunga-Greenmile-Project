# app/models.py

from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from app import db, login_manager
from datetime import datetime


class User(UserMixin, db.Model):
    """
    Create an Employee table
    """

    # Ensures table will be named in plural and not in singular
    # as is the name of the model
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(60), index=True, unique=True)
    username = db.Column(db.String(60), index=True, unique=True)
    first_name = db.Column(db.String(60), index=True)
    last_name = db.Column(db.String(60), index=True)
    password_hash = db.Column(db.String(128))
    package_id = db.Column(db.Integer, db.ForeignKey('packages.id'))
    is_admin = db.Column(db.Boolean, default=False)
    is_supplier = db.Column(db.Boolean, default=False)
    is_loader = db.Column(db.Boolean, default=False)
    is_recipient = db.Column(db.Boolean, default=False)


    @property
    def password(self):
        """
        Prevent pasword from being accessed
        """
        raise AttributeError('password is not a readable attribute.')

    @password.setter
    def password(self, password):
        """
        Set password to a hashed password
        """
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        """
        Check if hashed password matches actual password
        """
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User: {}>'.format(self.username)


# Set up user_loader
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

##########################################################################

class Package(db.Model):
    """
    Create a Package table
    """

    __tablename__ = 'packages'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60))
    date_created = db.Column(db.String(60))
    date_to_deliver = db.Column(db.String(60))
    addressed_to = db.Column(db.String(200))
    package_type = db.Column(db.String(200))
    hub = db.Column(db.String(200))
    description = db.Column(db.String(200))
    users = db.relationship('User', backref='package',
                                lazy='dynamic')

    def __repr__(self):
        return '<Package: {}>'.format(self.name)