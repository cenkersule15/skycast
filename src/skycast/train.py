import hashlib
import json
import math
import joblib
import numpy as np
import pandas as pd
from sklearn.ensemble import HistGradientBoostingRegressor
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_absolute_error, mean_squared_error
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from skycast.data import CITIES, ROOT, load_city
from skycast.features import supervised


def metrics(y, prediction):
    return {'mae': float(mean_absolute_error(y, prediction)), 'rmse': float(np.sqrt(mean_squared_error(y, prediction))), 'bias': float(np.mean(prediction - y))}


def predict(bundle, x):
    if bundle['name'] == 'Persistence':
        return x['temperature_2m_mean_lag1'].to_numpy()
    result = bundle['model'].predict(x)
    if bundle['name'] == 'Gradient boosting':
        result = result + x['temperature_2m_mean_lag1'].to_numpy()
    return result


def train():
    out = ROOT / 'artifacts'
    out.mkdir(exist_ok=True)
    reports, bundles, predictions = {}, {}, []
    for city in CITIES:
        x, y = supervised(load_city(city))
        masks = {'train': x.index.year <= 2020, 'validation': (x.index.year >= 2021) & (x.index.year <= 2022), 'calibration': x.index.year == 2023, 'test': x.index.year >= 2024}
        xt, yt = x.loc[masks['train']], y.loc[masks['train']]
        candidates = {'Ridge regression': make_pipeline(StandardScaler(), Ridge(alpha=10.0)), 'Gradient boosting': HistGradientBoostingRegressor(max_iter=180, learning_rate=.05, max_leaf_nodes=12, l2_regularization=5, early_stopping=False, random_state=42)}
        validation_scores = {'Persistence': metrics(y.loc[masks['validation']], x.loc[masks['validation'], 'temperature_2m_mean_lag1'])['mae']}
        fitted = {'Persistence': {'name': 'Persistence', 'model': None}}
        for name, model in candidates.items():
            target = yt - xt['temperature_2m_mean_lag1'] if name == 'Gradient boosting' else yt
            model.fit(xt, target)
            bundle = {'name': name, 'model': model}
            fitted[name] = bundle
            validation_scores[name] = metrics(y.loc[masks['validation']], predict(bundle, x.loc[masks['validation']]))['mae']
        selected = min(validation_scores, key=validation_scores.get)
        bundle = fitted[selected]
        cal_x, cal_y = x.loc[masks['calibration']], y.loc[masks['calibration']]
        residuals = np.abs(cal_y.to_numpy() - predict(bundle, cal_x))
        rank = min(len(residuals), math.ceil((len(residuals) + 1) * .9))
        radius = float(np.sort(residuals)[rank - 1])
        bundle.update({'interval_radius': radius, 'features': x.columns.tolist(), 'trained_until': '2020-12-31', 'city': city})
        bundles[city] = bundle
        test_x, test_y = x.loc[masks['test']], y.loc[masks['test']]
        month_means = yt.groupby(yt.index.month).mean()
        seasonal = test_x.index.month.map(month_means).to_numpy()
        table = {}
        for name, fitted_bundle in fitted.items():
            table[name] = metrics(test_y, predict(fitted_bundle, test_x))
        table['Seasonal mean'] = metrics(test_y, seasonal)
        pred = predict(bundle, test_x)
        lower, upper = pred - radius, pred + radius
        reports[city] = {'selected_model': selected, 'validation_mae': validation_scores, 'test_metrics': table, 'interval_radius': radius, 'interval_target_coverage': .9, 'test_interval_coverage': float(np.mean((test_y.to_numpy() >= lower) & (test_y.to_numpy() <= upper))), 'splits': {name: {'rows': int(mask.sum()), 'start': str(x.index[mask][0].date()), 'end': str(x.index[mask][-1].date())} for name, mask in masks.items()}, 'features': list(x.columns), 'source_csv_sha256': hashlib.sha256((ROOT / 'data' / f'{city}.csv').read_bytes()).hexdigest()}
        predictions.append(pd.DataFrame({'city': city, 'date': test_x.index, 'actual': test_y.to_numpy(), 'prediction': pred, 'persistence': test_x['temperature_2m_mean_lag1'].to_numpy(), 'lower': lower, 'upper': upper}))
        print(city, selected, round(table[selected]['mae'], 3), 'baseline', round(table['Persistence']['mae'], 3), flush=True)
    joblib.dump(bundles, out / 'models.joblib', compress=3)
    report = {'seed': 42, 'prediction_horizon': 'Next local calendar day after the final complete input day', 'data_period': '2010-01-01 / 2025-12-31', 'train_end': '2020-12-31', 'validation_period': '2021-2022', 'calibration_period': '2023', 'test_period': '2024-2025', 'training_note': 'No random split. Models fit on 2010-2020 only; validation selects model per city; 2023 sets absolute residual intervals; 2024-2025 is held out. Prior realised test-day weather becomes available for each successive retrospective one-step prediction. No refit on validation/calibration/test.', 'cities': reports}
    (out / 'report.json').write_text(json.dumps(report, indent=2) + '\n')
    pd.concat(predictions, ignore_index=True).to_csv(out / 'test_predictions.csv', index=False, float_format='%.6f')
    example = load_city('warsaw').tail(30)
    example.to_csv(ROOT / 'data' / 'example_history.csv', index=False)


if __name__ == '__main__':
    train()
