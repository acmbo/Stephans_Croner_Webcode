"""DB Models for Flask Marschmallow

for further information see : https://flask-marshmallow.readthedocs.io/en/latest/
"""
from extensions import ma
from extensions import ScrapperData, UsedKeywords, UsedKeywords_7days


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
    keyword = ma.auto_field()
    amount_of_uses = ma.auto_field()


class UsedKeyword_7daysSchema(ma.SQLAlchemySchema):
    class Meta:
        model = UsedKeywords_7days

    id = ma.auto_field()
    keyword = ma.auto_field()
    amount_of_uses = ma.auto_field()
