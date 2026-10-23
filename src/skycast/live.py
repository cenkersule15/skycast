import datetime as dt
import json
import urllib.parse
import urllib.request
from zoneinfo import ZoneInfo
import numpy as np
import pandas as pd
from skycast.data import CITIES

DAILY_FIELDS = ['temperature_2m_mean', 'temperature_2m_max', 'temperature_2m_min', 'precipitation_sum', 'precipitation_probability_max', 'wind_speed_10m_max']
CURRENT_FIELDS = ['temperature_2m', 'apparent_temperature', 'relative_humidity_2m', 'wind_speed_10m']


def local_today(city):
    return dt.datetime.now(ZoneInfo(CITIES[city]['timezone'])).date()


def parse_forecast(payload, today):
    if payload.get('error'):
        raise ValueError(payload.get('reason', 'Weather provider error.'))
    daily = pd.DataFrame(payload['daily']).rename(columns={'time': 'date'})
    daily['date'] = pd.to_datetime(daily['date'])
    expected = pd.date_range(today, periods=7, freq='D')
    daily = daily.loc[daily['date'].isin(expected)].sort_values('date').reset_index(drop=True)
    if not daily['date'].equals(pd.Series(expected, name='date')):
        raise ValueError('Provider response does not contain the current seven-day forecast.')
    if not np.isfinite(daily[DAILY_FIELDS].to_numpy(dtype=float)).all():
        raise ValueError('Forecast contains missing values.')
    current = payload['current']
    for field in CURRENT_FIELDS:
        if not np.isfinite(float(current[field])):
            raise ValueError('Current conditions contain missing values.')
    current_time = pd.Timestamp(current['time'])
    if abs((current_time.date() - today).days) > 0:
        raise ValueError('Current conditions have an unexpected date.')
    return {'daily': daily, 'current': current, 'timezone': payload['timezone'], 'fetched_at_utc': dt.datetime.now(dt.timezone.utc).isoformat()}


def fetch_forecast(city, today=None):
    if city not in CITIES:
        raise ValueError('Unsupported city.')
    today = today or local_today(city)
    spec = CITIES[city]
    query = urllib.parse.urlencode({'latitude': spec['latitude'], 'longitude': spec['longitude'], 'timezone': spec['timezone'], 'forecast_days': 7, 'daily': ','.join(DAILY_FIELDS), 'current': ','.join(CURRENT_FIELDS), 'temperature_unit': 'celsius', 'wind_speed_unit': 'kmh', 'precipitation_unit': 'mm'})
    url = 'https://api.open-meteo.com/v1/forecast?' + query
    with urllib.request.urlopen(url, timeout=15) as response:
        payload = json.loads(response.read())
    return parse_forecast(payload, today)
