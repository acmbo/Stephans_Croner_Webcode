"""further details about the process:
https://flask-marshmallow.readthedocs.io/en/latest/#flask_marshmallow.sqla.SQLAlchemyAutoSchema

For installation:
pip install -U flask-sqlalchemy marshmallow-sqlalchemy
"""

from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask import Response

from ormClasses import City, Country
from geopyOrm import get_all_citys, add_city, get_city_by_name, deleteCityByName

import os

geopyDBPath = os.path.join(os.getcwd(), "blueprints","operationalEndpoints","geopy", "geopydb.sqlite")

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{geopyDBPath}"

# Order matters: Initialize SQLAlchemy before Marshmallow
db = SQLAlchemy(app)
ma = Marshmallow(app)


class CitySchema(ma.SQLAlchemySchema):
    class Meta:
        model = City

    id = ma.auto_field()
    city_name = ma.auto_field()
    _long = ma.auto_field()
    _lat = ma.auto_field()
    state = ma.auto_field()
    country = ma.auto_field()

city = City(city_name = "Düsseldorf-Erkrath",
            _long = 51.233334,
            _lat = 6.783333,
            state = "NRW",
            country = "Germany")


citySchema = CitySchema()
#db.session.add(city)
#db.session.commit()
#citySchema.dump(city)

#get_all_citys, add_city, get_city_by_name



@app.route('/')
def example():
   return '{"name":"Bob"}'


@app.route("/api/citys/", methods=['POST', 'GET'])
def citys_open():
    
    if request.method == 'GET':
    
        citys = get_all_citys(db.session)
        citys_list = [citySchema.dump(city) for city in citys]
        return jsonify(citys_list)


@app.route("/api/city/", methods=['GET'])
def city_open():
    
    if request.method == 'GET':
        cityname = request.args.get('name')
        
        if cityname:
            citys = get_city_by_name(cityname, db.session)
            citys_list = [citySchema.dump(city) for city in citys]
            return jsonify(citys_list)
        else:
            return Response("Bad Request",
                            status=400,)
            
    


@app.route("/api/city", methods=['DELETE'])
def city_closed():
    #if request.method == 'POST':
    # Here check for right input
    if request.method == 'POST':
        print(request.form)
        print(type(request.form))
        check=True
        
        
        city_name = request.form.get('name')
        _long = float(request.form.get('long'))
        _lat = float(request.form.get('lat'))
        state = request.form.get('state')
        country = request.form.get('country')
        
        if check==True:
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
            status = deleteCityByName(db.session,cityname)
            return "", 204  
        
        else:
            return Response("Bad Request",
                            status=400,)
        

if __name__ == '__main__':
    app.run()