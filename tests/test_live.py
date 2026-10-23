import datetime as dt
import pytest
from skycast.live import parse_forecast


def test_seven_day_forecast_starts_on_local_today(live_payload):
    today=dt.date(2026,10,23)
    result=parse_forecast(live_payload(today),today)
    assert result['daily']['date'].iloc[0].date()==today
    assert result['daily']['date'].iloc[-1].date()==today+dt.timedelta(days=6)


@pytest.mark.parametrize('kind',['stale','missing','provider_error'])
def test_invalid_or_stale_forecast_is_rejected(live_payload,kind):
    today=dt.date(2026,10,23)
    payload=live_payload(today)
    if kind=='stale':
        payload=live_payload(today-dt.timedelta(days=1))
    elif kind=='missing':
        payload['daily']['temperature_2m_mean'][2]=None
    else:
        payload={'error':True,'reason':'Rate limited'}
    with pytest.raises(ValueError):parse_forecast(payload,today)
