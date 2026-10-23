from pathlib import Path
import hashlib
import json
import urllib.parse
import urllib.request
import urllib.error
import time
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[2]
CITIES = {
    'warsaw': {'name': 'Warsaw', 'latitude': 52.23, 'longitude': 21.01, 'timezone': 'Europe/Warsaw', 'country': 'Poland'},
    'istanbul': {'name': 'Istanbul', 'latitude': 41.01, 'longitude': 28.98, 'timezone': 'Europe/Istanbul', 'country': 'Türkiye'},
    'berlin': {'name': 'Berlin', 'latitude': 52.52, 'longitude': 13.41, 'timezone': 'Europe/Berlin', 'country': 'Germany'},
    'paris': {'name': 'Paris', 'latitude': 48.86, 'longitude': 2.35, 'timezone': 'Europe/Paris', 'country': 'France'},
    'london': {'name': 'London', 'latitude': 51.51, 'longitude': -0.13, 'timezone': 'Europe/London', 'country': 'United Kingdom'},
    'rome': {'name': 'Rome', 'latitude': 41.90, 'longitude': 12.50, 'timezone': 'Europe/Rome', 'country': 'Italy'},
    'madrid': {'name': 'Madrid', 'latitude': 40.42, 'longitude': -3.70, 'timezone': 'Europe/Madrid', 'country': 'Spain'},
    'ankara': {'name': 'Ankara', 'latitude': 39.93, 'longitude': 32.86, 'timezone': 'Europe/Istanbul', 'country': 'Türkiye'},
}
WEATHER = ['temperature_2m_mean', 'temperature_2m_max', 'temperature_2m_min', 'precipitation_sum', 'wind_speed_10m_max', 'shortwave_radiation_sum']


def validate_daily(frame):
    required = ['date', *WEATHER]
    missing = sorted(set(required) - set(frame.columns))
    if missing:
        raise ValueError('Missing columns: ' + ', '.join(missing))
    f = frame[required].copy()
    f['date'] = pd.to_datetime(f['date'], errors='raise')
    if f['date'].dt.tz is not None:
        raise ValueError('Dates must be timezone-free local calendar dates.')
    if not (f['date'] == f['date'].dt.normalize()).all():
        raise ValueError('Use one local calendar date per row, without times.')
    f = f.sort_values('date').reset_index(drop=True)
    if f['date'].duplicated().any():
        raise ValueError('Duplicate dates are not allowed.')
    if len(f) < 14:
        raise ValueError('Provide at least 14 consecutive complete days.')
    if not f['date'].diff().iloc[1:].eq(pd.Timedelta(days=1)).all():
        raise ValueError('Dates must be consecutive, without missing days.')
    for col in WEATHER:
        f[col] = pd.to_numeric(f[col], errors='raise')
    if not np.isfinite(f[WEATHER].to_numpy(dtype=float)).all():
        raise ValueError('All weather values must be finite numbers.')
    if (f['temperature_2m_min'] > f['temperature_2m_mean']).any() or (f['temperature_2m_mean'] > f['temperature_2m_max']).any():
        raise ValueError('Daily temperature must satisfy minimum <= mean <= maximum.')
    if (f[WEATHER[:3]].abs() > 70).any().any():
        raise ValueError('Temperature must be between -70 and 70 Celsius.')
    if (f[WEATHER[3:]] < 0).any().any():
        raise ValueError('Precipitation, wind and radiation cannot be negative.')
    if (f['wind_speed_10m_max'] > 300).any() or (f['shortwave_radiation_sum'] > 60).any() or (f['precipitation_sum'] > 1000).any():
        raise ValueError('Weather values exceed the supported input range.')
    return f


def load_city(city):
    if city not in CITIES:
        raise ValueError('Unsupported city.')
    return validate_daily(pd.read_csv(ROOT / 'data' / f'{city}.csv'))


def download():
    destination = ROOT / 'data'
    destination.mkdir(exist_ok=True)
    records = []
    for city, spec in CITIES.items():
        query = urllib.parse.urlencode({'latitude': spec['latitude'], 'longitude': spec['longitude'], 'start_date': '2010-01-01', 'end_date': '2025-12-31', 'daily': ','.join(WEATHER), 'models': 'era5', 'timezone': spec['timezone']})
        url = 'https://archive-api.open-meteo.com/v1/archive?' + query
        cached = destination / f'{city}.csv'
        if cached.exists():
            f = validate_daily(pd.read_csv(cached))
            records.append({'city': city, 'request_url': url, 'csv_sha256': hashlib.sha256(cached.read_bytes()).hexdigest(), 'rows': len(f)})
            print(city, len(f), 'cached', flush=True)
            continue
        for attempt in range(4):
            try:
                with urllib.request.urlopen(url, timeout=90) as response:
                    raw = response.read()
                break
            except urllib.error.HTTPError as error:
                if error.code != 429 or attempt == 3:
                    raise
                print(city, 'rate limit; retrying', flush=True)
                time.sleep(25)
        payload = json.loads(raw)
        f = validate_daily(pd.DataFrame(payload['daily']).rename(columns={'time': 'date'}))
        f['date'] = f['date'].dt.strftime('%Y-%m-%d')
        f.to_csv(destination / f'{city}.csv', index=False)
        records.append({'city': city, 'request_url': url, 'returned_latitude': payload['latitude'], 'returned_longitude': payload['longitude'], 'raw_response_sha256': hashlib.sha256(raw).hexdigest(), 'csv_sha256': hashlib.sha256((destination / f'{city}.csv').read_bytes()).hexdigest(), 'units': payload['daily_units'], 'rows': len(f)})
        print(city, len(f), flush=True)
    meta = {'provider': 'Open-Meteo Historical Weather API', 'dataset': 'ECMWF / Copernicus ERA5 reanalysis', 'licence': 'CC BY 4.0', 'documentation': 'https://open-meteo.com/en/docs/historical-weather-api', 'downloaded_at_utc': pd.Timestamp.now(tz='UTC').isoformat(), 'cities': records}
    (destination / 'provenance.json').write_text(json.dumps(meta, indent=2) + '\n')


if __name__ == '__main__':
    download()
