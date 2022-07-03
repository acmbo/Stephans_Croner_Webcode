from flask import Blueprint, Response, jsonify, request, abort

from .ormClasses import City, Country
from .geopyOrm import get_all_citys, add_city, get_city_by_name, deleteCityByName,\
    get_all_countrys, get_country_by_name, deleteCountryByName, add_country
from .models import CitySchema, CountrySchema
from extensions import db

blueprint = Blueprint('geopyapi', __name__, url_prefix='/geo')

# DB Schema


citySchema = CitySchema()
countrySchema = CountrySchema()


@blueprint.route('/')
def example():
    abort(404)
    # return '{"test":"Hello World"}'


@blueprint.route("/cities/", methods=['GET'])
def citys_open():
    """
    Open Api Routes for a all cities. Get function will return information of all cities in db.

    Returns:
        json or bad request: city long, lat information from db
    """
    if request.method == 'GET':

        citys = get_all_citys(db.session)
        citys_list = [citySchema.dump(city) for city in citys]
        return jsonify(citys_list)


@blueprint.route("/city/", methods=['GET'])
def city_open():
    """
    Open Api Routes for a single city. Get function will return information of one city.

    Request Args:
        - name : Name of a city

    Returns:
        json or bad request: city long, lat information from db
    """
    if request.method == 'GET':
        cityname = request.args.get('name')

        if cityname:
            citys = get_city_by_name(cityname, db.session)
            citys_list = [citySchema.dump(city) for city in citys]
            return jsonify(citys_list)
        else:
            return Response("Bad Request",
                            status=400,)


@blueprint.route("/countries/", methods=['GET'])
def countries_open():
    """
    Open Api Routes for a all country. Get function will return information of all countries in db.

    Returns:
        json or bad request: countrys long, lat information from db
    """
    if request.method == 'GET':

        countrys = get_all_countrys(db.session)
        country_list = [countrySchema.dump(count) for count in countrys]
        return jsonify(country_list)


@blueprint.route("/country/", methods=['GET'])
def country_open():
    """
    Open Api Routes for a single country. Get function will return information of one country.

    Request Args:
        - name : Name of a country

    Returns:
        json or bad request: country long, lat information from db
    """
    if request.method == 'GET':
        countryname = request.args.get('name')

        if countryname:
            countrys = get_country_by_name(countryname, db.session)
            country_list = [countrySchema.dump(count) for count in countrys]
            return jsonify(country_list)
        else:
            return Response("Bad Request",
                            status=400,)


@blueprint.route("/city", methods=['POST', 'DELETE'])
def city_closed():
    """
    Api Route with authentification for a single city. Deletes a single City from the db with DELETE request. Adds a city with POST request.

    Request Args:
        - name : Name of a city
        - long : longitude coordinates
        - lat : latidue coordinates
        - state : state, which city belongs to
        - country : country, which city belongs to

    """
    # if request.method == 'POST':
    # Here check for right input
    if request.method == 'POST':
        print(request.form)
        print(type(request.form))
        check = True

        city_name = request.form.get('name')
        _long = float(request.form.get('long'))
        _lat = float(request.form.get('lat'))
        state = request.form.get('state')
        country = request.form.get('country')

        if check == True:
            add_city(db.session,
                     city_name,
                     _long,
                     _lat,
                     state,
                     country,
                     None)
            return "", 204
        else:
            return Response("Bad Post",
                            status=400,)

    if request.method == 'DELETE':

        cityname = request.args.get('name')

        if cityname:
            status = deleteCityByName(db.session, cityname)
            return "", 204

        else:
            return Response("Bad Request",
                            status=400,)


@blueprint.route("/country", methods=['POST', 'DELETE'])
def country_closed():
    """
    Api Route with authentification for a single country. Deletes a single country from the db with DELETE request. Adds a country with POST request.

    Request Args:
        - name : Name of a country
        - long : longitude coordinates
        - lat : latidue coordinates
        - polstate : political state, which country belongs to

    """
    # if request.method == 'POST':
    # Here check for right input
    if request.method == 'POST':
        print(request.form)
        print(type(request.form))
        check = True

        country_name = request.form.get('name')
        _long = float(request.form.get('long'))
        _lat = float(request.form.get('lat'))
        polstate = request.form.get('state')

        if check == True:
            add_country(db.session,
                        country_name,
                        _long,
                        _lat,
                        polstate)
            return "", 204
        else:
            return Response("Bad Post",
                            status=400,)

    if request.method == 'DELETE':

        countryname = request.args.get('name')

        if countryname:
            status = deleteCountryByName(db.session, countryname)
            return "", 204

        else:
            return Response("Bad Request",
                            status=400,)


if __name__ == "__main__":

    city = City(city_name="Düsseldorf-Erkrath",
                _long=51.233334,
                _lat=6.783333,
                state="NRW",
                country="Germany")
