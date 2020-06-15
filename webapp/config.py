import os

basedir = os.path.abspath(os.path.dirname(__file__))
WEATHER_DEFAULT_CITY = "CO45XW"
WEATHER_API_KEY = "5b2edb59c6eb41daa06191242200206"
WEATHER_URL = "http://api.worldweatheronline.com/premium/v1/weather.ashx"
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, '..', 'webapp.db')