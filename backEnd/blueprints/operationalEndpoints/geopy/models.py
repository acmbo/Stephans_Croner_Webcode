"""DB Models for Flask Marschmallow

for further information see : https://flask-marshmallow.readthedocs.io/en/latest/
"""
from extensions import ma
from .ormClasses import City, Country


class CitySchema(ma.SQLAlchemySchema):
    class Meta:
        model = City

    id = ma.auto_field()
    city_name = ma.auto_field()
    _long = ma.auto_field()
    _lat = ma.auto_field()
    state = ma.auto_field()
    country = ma.auto_field()


class CountrySchema(ma.SQLAlchemySchema):
    class Meta:
        model = Country

    id = ma.auto_field()
    country_name = ma.auto_field()
    _long = ma.auto_field()
    _lat = ma.auto_field()
    political_state = ma.auto_field()
