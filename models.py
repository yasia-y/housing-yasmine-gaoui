#models.py
from database import db  

class House(db.Model):
    __tablename__ = 'houses'

    id = db.Column(db.Integer, primary_key=True)
    longitude = db.Column(db.Float, nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    housing_median_age = db.Column(db.Integer, nullable=False)
    total_rooms = db.Column(db.Integer, nullable=False)
    total_bedrooms = db.Column(db.Integer, nullable=False)
    population = db.Column(db.Integer, nullable=False)
    households = db.Column(db.Integer, nullable=False)
    median_income = db.Column(db.Float, nullable=False)
    median_house_value = db.Column(db.Float, nullable=False)
    ocean_proximity = db.Column(db.String, nullable=False)
    
    def __repr__(self):
        return f"<House {self.id}, {self.ocean_proximity}>"


    def to_dict(self):
        return {
            'id': self.id,
            'longitude': self.longitude,
            'latitude': self.latitude,
            'housing_median_age': self.housing_median_age,
            'total_rooms': self.total_rooms,
            'total_bedrooms': self.total_bedrooms,
            'population': self.population,
            'households': self.households,
            'median_income': self.median_income,
            'median_house_value': self.median_house_value,
            'ocean_proximity': self.ocean_proximity
        }
