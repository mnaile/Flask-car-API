from flask import Flask
from extensions.extensions import db

class Car(db.Model):
    __tablename__="Car"

    id = db.Column(db.Integer(), primary_key=True)
    mark = db.Column(db.String(), nullable=True)
    model = db.Column(db.String(), nullable=True)
    color = db.Column(db.String(), nullable=True)
    manufacture_year = db.Column(db.Integer(), nullable=True)

    def save_db(self):
        db.session.add(self)
        db.session.commit()
        return self

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
        return self

    def update_db(self, **kwargs):
        for key, val in kwargs.items():
            setattr(self, key, val)
        self.save_db()