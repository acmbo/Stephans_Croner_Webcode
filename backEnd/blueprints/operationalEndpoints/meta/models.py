"""DB Models for Flask Marschmallow

for further information see : https://flask-marshmallow.readthedocs.io/en/latest/
"""
from extensions import ma
from .ormClasses import ScrapperData, UsedKeywords


class ScrapperDataSchema(ma.SQLAlchemySchema):
    class Meta:
        model = ScrapperData

    id = ma.auto_field()
    scrapper_name = ma.auto_field()
    amount_of_db_entries = ma.auto_field()
    entrydate = ma.auto_field()
    errors = ma.auto_field()


class UsedKeywordSchema(ma.SQLAlchemySchema):
    class Meta:
        model = UsedKeywords

    id = ma.auto_field()
    keywords = ma.auto_field()
    amount_of_uses = ma.auto_field()
