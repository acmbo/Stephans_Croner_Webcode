"""DB Models for Flask Marschmallow

for further information see : https://flask-marshmallow.readthedocs.io/en/latest/
"""
from extensions import ma
from extensions import ThemeGraphDaily, ThemeGraphMonthly, ThemeGraphWeekly


class ThemeGraphDailySchema(ma.SQLAlchemySchema):
    class Meta:
        model = ThemeGraphDaily

    id = ma.auto_field()
    source = ma.auto_field()
    target = ma.auto_field()
    value = ma.auto_field()
    urls = ma.auto_field()


class ThemeGraphWeeklySchema(ma.SQLAlchemySchema):
    class Meta:
        model = ThemeGraphWeekly

    id = ma.auto_field()
    source = ma.auto_field()
    target = ma.auto_field()
    value = ma.auto_field()
    urls = ma.auto_field()


class ThemeGraphMonthlySchema(ma.SQLAlchemySchema):
    class Meta:
        model = ThemeGraphMonthly

    id = ma.auto_field()
    source = ma.auto_field()
    target = ma.auto_field()
    value = ma.auto_field()
    urls = ma.auto_field()
