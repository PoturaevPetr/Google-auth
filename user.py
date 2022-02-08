from flask_login import UserMixin
from db import get_db
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()


class User(UserMixin):
    def __init__(self, id_, name, email, profile_pic, balance, date):
        self.id = id_
        self.name = name
        self.email = email
        self.profile_pic = profile_pic
        self.date = date
        self.balance = balance

    @staticmethod
    def get(user_id):
        db = get_db()
        user = db.execute(
            "SELECT * FROM user WHERE id = ?", (user_id,)
        ).fetchone()
        if not user:
            return None

        user = User(
            id_=user[0], name=user[1], email=user[2], profile_pic=user[3], date=user[4], balance=user[5])
        return user

    @staticmethod
    def create(id_, name, email, profile_pic, date, balance):
        db = get_db()
        db.execute(
            "INSERT INTO user (id, name, email, profile_pic, date, balance) "
            "VALUES (?, ?, ?, ?, ?, ?)",
            (id_, name, email, profile_pic, date, balance),
        )
        db.commit()




class Service(db.Model):
    __tablename__ = 'service'
    id = db.Column(db.Integer, primary_key=True)
    service = db.Column(db.String(200), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String(120), nullable=False)

    def __init__(self, servise, price, status):
        self.service = servise
        self.price = price
        self.status = status

class History(db.Model):
    __tablename__ = 'history'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(200), nullable=False)
    service = db.Column(db.String(200), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    balance = db.Column(db.Integer, nullable=False)

    def __init__(self, date, service, price, balance):
        self.date = date
        self.service = service
        self.price = price
        self.balance = balance



class Payments(db.Model):
    __tablename__ = 'payments'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(200), nullable=False)
    service = db.Column(db.String(200), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String(200), nullable=False)

    def __init__(self, date, service, price, status):
        self.date = date
        self.service = service
        self.price = price
        self.status = status

    def update(cls, **new_data):
        try:
            print(new_data)
            query = cls.query().filter_by(id == new_data.get('id')).first()
            query.description = [new_data.get('id'),
                                 new_data.get('service'),
                                 new_data.get('price'),
                                 new_data.get('Оплачено')]
            cls.session.commit()
        except:
            cls.session.rollback()
            return {'error': 'error'}
        return True

    def get_pay(cls, **kwargs):
        id = kwargs.get('id')

        if not id:
            return None

        pay = cls.query.filter_by(id=id).first()

        return pay