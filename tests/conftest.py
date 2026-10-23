import datetime as dt
import pytest
from skycast.live import parse_forecast


@pytest.fixture
def live_payload():
    def make(today):
        return {'timezone': 'Europe/Warsaw', 'daily': {'time': [(today+dt.timedelta(days=i)).isoformat() for i in range(7)], 'temperature_2m_mean': [12.0]*7, 'temperature_2m_max': [16.0]*7, 'temperature_2m_min': [8.0]*7, 'precipitation_sum': [1.0]*7, 'precipitation_probability_max': [30]*7, 'wind_speed_10m_max': [20.0]*7}, 'current': {'time': today.isoformat()+'T12:00', 'temperature_2m': 13.0, 'apparent_temperature': 11.0, 'relative_humidity_2m': 65.0, 'wind_speed_10m': 12.0}}
    return make


@pytest.fixture(autouse=True)
def mock_live_provider(monkeypatch, live_payload):
    monkeypatch.setattr('skycast.live.fetch_forecast', lambda city,today: parse_forecast(live_payload(today),today))
