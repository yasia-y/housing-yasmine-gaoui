from flask import Flask, jsonify, request
from models import House, db

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Housing API!"

@app.route('/houses', methods=['POST'])
def add_house():
    # Logique pour ajouter une maison
    new_house = House(
        longitude=request.json['longitude'],
        latitude=request.json['latitude'],
        housing_median_age=request.json['housing_median_age'],
        total_rooms=request.json['total_rooms'],
        total_bedrooms=request.json['total_bedrooms'],
        population=request.json['population'],
        households=request.json['households'],
        median_income=request.json['median_income'],
        median_house_value=request.json['median_house_value'],
        ocean_proximity=request.json['ocean_proximity']
    )
    db.session.add(new_house)
    db.session.commit()
    return jsonify(new_house.to_dict()), 201

if __name__ == '__main__':
    app.run(debug=True)
