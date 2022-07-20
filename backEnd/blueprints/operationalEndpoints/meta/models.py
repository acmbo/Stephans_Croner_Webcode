"""DB Models for Flask Marschmallow

for further information see : https://flask-marshmallow.readthedocs.io/en/latest/
"""
from extensions import ma
from extensions import ScrapperData, UsedKeywords, UsedKeywords_7days, Postings_weekly, Postings_montly, Postings_year


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


class Postings_weeklySchema(ma.SQLAlchemySchema):
    class Meta:
        model = Postings_weekly

    id = ma.auto_field()
    date = ma.auto_field()
    post = ma.auto_field()


class Postings_montlySchema(ma.SQLAlchemySchema):
    class Meta:
        model = Postings_montly

    id = ma.auto_field()
    date = ma.auto_field()
    post = ma.auto_field()


class Postings_yearSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Postings_year

    id = ma.auto_field()
    date = ma.auto_field()
    post = ma.auto_field()
