import darksky
from datetime import date, timedelta, datetime
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut
import numpy as np
import sys
import time
import geocoder


def geolocate_city(city):
    g = geocoder.google(city)
    try:
        location = g.geojson['features'][0]['geometry']['coordinates']
    except (IndexError, TypeError):
        location = None
    coord = (tuple(location) if (location is not None) else (None, None))

    return coord


def get_forecast(location):

    coord = geolocate_city(location)
    key = '1136ef786eb77b372c671b0b22ae1e0f'

    print(f'Checking weather for {location}')
    data = []
    with darksky.forecast(key, *coord) as geo_data:
        for hour in range(len(geo_data.hourly)-38):
            hourofforecast = datetime.now().hour + hour if datetime.now().hour + \
                hour < 24 else datetime.now().hour + hour - 24
            hour = dict(time=str(hourofforecast).zfill(2) + ':' + str(datetime.now().minute),
                        summary=geo_data.hourly[hour].summary,
                        temperature=np.round(
                            (geo_data.hourly[hour].temperature-32)*.5556, 2),
                        prec_int=np.round(
                            geo_data.hourly[hour].precipIntensity, 2),
                        prec_prob=np.round(geo_data.hourly[hour].precipProbability*100, 0))

            hourly_data = 'At {time}: {summary}, {temperature}°C. Rain prob {prec_prob}% ({prec_int} mm)'.format(
                **hour)
            data.append(hourly_data)
    return 'Hello world'
