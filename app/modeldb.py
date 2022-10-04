# -*- coding: utf-8 -*-

# import bcrypt
from sqlalchemy.sql import func
from sqlalchemy.exc import IntegrityError
from flask_sqlalchemy import SQLAlchemy

 # instantiating SQLAlchemy
db = SQLAlchemy()

class Roles(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    users = db.relationship('Users', backref='role')

    def __repr__(self):
        return '<Role %r>' % self.name

    def init_roles(self):
        admin_role = Roles(id=1, name='Admin')
        pilote_role = Roles(id=2, name='Pilot')
        user_role = Roles(id=3, name='User')
        db.session.add(admin_role)
        db.session.add(pilote_role)
        db.session.add(user_role)
        try:
            db.session.commit()
        except IntegrityError:
            db.session.rollback()


class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column("id", db.BigInteger().with_variant(db.Integer, "sqlite"), primary_key=True)
    docid = db.Column(db.Integer, unique=True, nullable=False)
    first_name = db.Column(db.String(80), unique=False, nullable=False)
    last_name = db.Column(db.String(80), unique=False, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    user_verification = db.Column(db.String(100))
    user_active = db.Column(db.String(2))
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    # repr method represents how one object of this datatable
    def __repr__(self):
        return '<Users %r>' % self.docid
        # return f"Name : {self.first_name}, LastName: {self.last_name}"

    def verify_password(self, password):
        pwhash = bcrypt.hashpw(password, self.password)
        return self.password == pwhash

    def add_user(self, cc, nombre, apellido, email, password):
        # password = str(Users().verify_password(password.encode('utf-8')))
        new_user = Users(docid=cc, first_name=nombre, last_name=apellido, email=email, password=password,
                         role_id=3)
        db.session.add(new_user)
        try:
            db.session.commit()
        except IntegrityError:
            db.session.rollback()


def start_db():
    db.create_all()

