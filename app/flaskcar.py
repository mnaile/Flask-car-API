from flask import Flask, request, jsonify
from app.model import Car
from app.serializer import CarSchema, CarUpdateSchema
from app_init.app_factory import create_app
from http import HTTPStatus
from marshmallow import ValidationError
import os
 
settings_name = os.getenv("settings")
app = create_app(settings_name)

#CREATE CAR

@app.route('/car', methods=["POST"])
def create_car():
    car_info = request.get_json()

    try:
        car = CarSchema().load(car_info)
        car.save_db()
    except ValidationError as err:
        return jsonify(err.messages),HTTPStatus.BAD_REQUEST

    return CarSchema().jsonify(car),HTTPStatus.OK

#READ CAR

@app.route('/car', methods=["GET"])
def get_all_car():
    car_info = Car.query.all()
    return CarSchema().jsonify(car_info, many=True),HTTPStatus.OK

@app.route('/car/<int:id>', methods=["GET"])
def get_car(id):
    car_info = Car.query.get(id)
    if car_info:
        return CarSchema().jsonify(car_info),HTTPStatus.OK
    return jsonify(msg="Not found"),HTTPStatus.NOT_FOUND

#DELETED CAR

@app.route('/car/<int:id>', methods=["DELETE"])
def delete_car(id):
    car_info = Car.query.get(id)
    if car_info:
        car_info.delete_from_db()
        return jsonify(msg="Car deleted"),HTTPStatus.OK
    return jsonify(msg="Not found"),HTTPStatus.NOT_FOUND

#UPDATE CAR

@app.route('/car/<int:id>', methods=["PUT"])
def update_car(id):
    car_info = Car.query.get(id)
    if car_info:
        newcar = request.get_json()
        newcar = CarUpdateSchema().load(newcar)
        car_info.update_db(**newcar)
        return CarSchema().jsonify(newcar),HTTPStatus.OK
    return jsonify(msg="Not found"),HTTPStatus.NOT_FOUND




