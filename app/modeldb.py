
# import bcrypt
from sqlalchemy.sql import func
from sqlalchemy.exc import IntegrityError
from flask_sqlalchemy import SQLAlchemy


# instantiating SQLAlchemy
db = SQLAlchemy()

class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column("id", db.BigInteger().with_variant(db.Integer, "sqlite"), primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    salt = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())
    links = db.relationship("ForgotLink", backref="user")

    # repr method represents how one object of this datatable
    def __repr__(self):
        return '<Users %r>' % self.docid
        # return f"Name : {self.first_name}, LastName: {self.last_name}"

    def verify_password(self, password):
        pass
        # pwhash = bcrypt.hashpw(password, self.password)
        # return self.password == pwhash

    def add_user(self, nombre, password, email):
        # password = str(Users().verify_password(password.encode('utf-8')))
        new_user = Users(username=nombre, password=password, email=email, salt=0)
        db.session.add(new_user)
        try:
            db.session.commit()
        except IntegrityError:
            db.session.rollback()


class ForgotLink(db.Model):
    __tablename__ = 'forgotlink'
    id = db.Column("id", db.BigInteger().with_variant(db.Integer, "sqlite"), primary_key=True)
    challenge = db.Column(db.String(100), nullable=False)
    created = db.Column(db.DateTime(timezone=True), server_default=func.now())
    validuntil = db.Column(db.DateTime(timezone=True), server_default=func.now())
    userid = db.Column(db.Integer, db.ForeignKey("users.id"))





def start_db():
    db.create_all()

