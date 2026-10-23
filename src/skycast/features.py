import numpy as np
import pandas as pd
from skycast.data import WEATHER, validate_daily


def features(frame):
    f = validate_daily(frame).set_index('date')
    x = pd.DataFrame(index=f.index)
    for col in WEATHER:
        x[col + '_lag1'] = f[col].shift(1)
    temp = f['temperature_2m_mean']
    for lag in [2, 3, 7, 14]:
        x[f'temperature_lag{lag}'] = temp.shift(lag)
    for window in [3, 7, 14]:
        x[f'temperature_mean{window}'] = temp.shift(1).rolling(window).mean()
    x['temperature_change'] = temp.shift(1) - temp.shift(2)
    x['temperature_range_lag1'] = (f['temperature_2m_max'] - f['temperature_2m_min']).shift(1)
    day = x.index.dayofyear.to_numpy()
    x['year_sin'] = np.sin(2 * np.pi * day / 365.25)
    x['year_cos'] = np.cos(2 * np.pi * day / 365.25)
    return x


def supervised(frame):
    f = validate_daily(frame)
    x = features(f)
    y = f.set_index('date')['temperature_2m_mean']
    keep = x.notna().all(axis=1)
    return x.loc[keep], y.loc[keep]


def next_features(frame):
    f = validate_daily(frame)
    last = f.iloc[-1].copy()
    last['date'] += pd.Timedelta(days=1)
    extended = pd.concat([f, last.to_frame().T], ignore_index=True)
    return features(extended).iloc[[-1]]
