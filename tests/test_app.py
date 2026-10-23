from pathlib import Path
import pytest
from streamlit.testing.v1 import AppTest


@pytest.mark.parametrize('language', ['English','Deutsch','Türkçe'])
def test_all_views_and_cities(language):
    app = AppTest.from_file(str(Path(__file__).resolve().parents[1]/'app.py'),default_timeout=30).run()
    app.sidebar.radio[0].set_value('overview').run()
    app.sidebar.selectbox[0].select(language).run()
    for city in ['warsaw','istanbul','berlin','paris','london','rome','madrid','ankara']:
        app.sidebar.selectbox[1].select(city).run()
        assert not app.exception
        assert len(app.metric) == 2
    for page in ['lab','validation']:
        app.sidebar.radio[0].set_value(page).run()
        assert not app.exception
        assert len(app.metric) == 3


@pytest.mark.parametrize('language', ['English','Deutsch','Türkçe'])
def test_live_forecast_view(language):
    app = AppTest.from_file(str(Path(__file__).resolve().parents[1]/'app.py'),default_timeout=30).run()
    app.sidebar.selectbox[0].select(language).run()
    assert app.sidebar.radio[0].value == 'live'
    assert not app.exception
    assert len(app.metric) == 4
    assert len(app.dataframe[0].value) == 7
    assert len(app.info) == 1


def test_live_api_failure_shows_error_without_historical_substitution(monkeypatch):
    import datetime as dt
    monkeypatch.setattr('skycast.live.local_today', lambda city: dt.date(2040,1,1))
    def fail(*args):
        raise OSError('Connection failed')
    monkeypatch.setattr('skycast.live.fetch_forecast',fail)
    app = AppTest.from_file(str(Path(__file__).resolve().parents[1]/'app.py'),default_timeout=30).run()
    assert not app.exception
    assert len(app.error) == 1
    assert len(app.metric) == 0
    app.sidebar.radio[0].set_value('overview').run()
    assert not app.exception
    assert len(app.metric) == 2
