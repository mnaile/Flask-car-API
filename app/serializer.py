from flask import Flask
from app.model import Car
from marshmallow import fields, validate
from extensions.extensions import ma

class CarSchema(ma.SQLAlchemyAutoSchema):

    mark = fields.String(required=True, validate=[validate.Length(min=1, max=40)])
    model = fields.String(required=True, validate=[validate.Length(min=2, max=40)])
    color = fields.String(required=True, validate=[validate.Length(min=2, max=40)])
    manufacture_year = fields.Integer(required=True)

    class Meta:
        model = Car
        load_instance = True

class CarUpdateSchema(ma.SQLAlchemySchema):

    mark = fields.String(validate=[validate.Length(min=1, max=40)])
    model = fields.String(validate=[validate.Length(min=2, max=40)])
    color = fields.String(validate=[validate.Length(min=2, max=40)])
    manufacture_year = fields.Integer()



