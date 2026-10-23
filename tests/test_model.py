import hashlib
import json
import joblib
import numpy as np
import pandas as pd
import pytest
from skycast.data import CITIES, ROOT, load_city, validate_daily
from skycast.features import features, next_features, supervised
from skycast.train import predict


def test_future_values_cannot_change_target_day_features():
    frame = load_city('warsaw').iloc[:60].copy()
    original = features(frame)
    changed = frame.copy()
    changed.loc[30:, 'temperature_2m_mean'] += 1
    changed.loc[30:, 'temperature_2m_max'] += 1
    changed.loc[30:, 'temperature_2m_min'] += 1
    pd.testing.assert_frame_equal(original.iloc[:31], features(changed).iloc[:31])
    assert not original.iloc[31:].equals(features(changed).iloc[31:])


def test_next_day_uses_last_complete_day_and_fourteen_day_history():
    frame = load_city('warsaw').iloc[:14]
    x = next_features(frame)
    assert x.index[0] == frame['date'].iloc[-1] + pd.Timedelta(days=1)
    assert x['temperature_2m_mean_lag1'].iloc[0] == frame['temperature_2m_mean'].iloc[-1]
    assert x['temperature_lag14'].iloc[0] == frame['temperature_2m_mean'].iloc[0]
    assert x['temperature_mean14'].iloc[0] == pytest.approx(frame['temperature_2m_mean'].mean())
    assert np.isfinite(x.to_numpy()).all()


@pytest.mark.parametrize('kind', ['missing', 'duplicate', 'gap', 'nan', 'negative', 'short', 'inconsistent'])
def test_invalid_history_is_rejected(kind):
    frame = load_city('warsaw').tail(30).copy()
    if kind == 'missing':
        frame = frame.drop(columns='precipitation_sum')
    elif kind == 'duplicate':
        frame.iloc[-1,0] = frame.iloc[-2,0]
    elif kind == 'gap':
        frame = frame.drop(frame.index[4])
    elif kind == 'nan':
        frame.iloc[0,1] = np.nan
    elif kind == 'negative':
        frame.loc[frame.index[0], 'precipitation_sum'] = -1
    elif kind == 'short':
        frame = frame.tail(13)
    else:
        frame.loc[frame.index[0], 'temperature_2m_min'] = 69
    with pytest.raises(ValueError):
        validate_daily(frame)


@pytest.mark.parametrize('city', list(CITIES))
def test_artifacts_reproduce_held_out_results(city):
    report = json.loads((ROOT/'artifacts/report.json').read_text())['cities'][city]
    model = joblib.load(ROOT/'artifacts/models.joblib')[city]
    x,y = supervised(load_city(city))
    test = x.index.year >= 2024
    prediction = predict(model,x.loc[test])
    assert float(np.abs(prediction-y.loc[test]).mean()) == pytest.approx(report['test_metrics'][model['name']]['mae'])
    assert report['source_csv_sha256'] == hashlib.sha256((ROOT/'data'/f'{city}.csv').read_bytes()).hexdigest()
    assert report['splits']['train']['end'] < report['splits']['validation']['start']
    assert report['splits']['validation']['end'] < report['splits']['calibration']['start']
    assert report['splits']['calibration']['end'] < report['splits']['test']['start']
    assert report['splits']['test']['rows'] == 731
    assert model['name'] == min(report['validation_mae'],key=report['validation_mae'].get)
