import datetime as dt
import json
import joblib
import pandas as pd
import plotly.graph_objects as go
import streamlit as st
from skycast.data import CITIES, ROOT, WEATHER, load_city, validate_daily
from skycast.features import next_features
from skycast.train import predict
from skycast.ui import CITY_LABELS, CSS, TEXT, BRAND_ICON, hero_markup, forecast_strip
import skycast.live as weather_live

st.set_page_config(page_title='SkyCast | Weather Intelligence', page_icon='☀', layout='wide')
st.markdown(CSS, unsafe_allow_html=True)


@st.cache_resource
def resources():
    return joblib.load(ROOT / 'artifacts/models.joblib'), json.loads((ROOT / 'artifacts/report.json').read_text())


@st.cache_data
def predictions():
    return pd.read_csv(ROOT / 'artifacts/test_predictions.csv', parse_dates=['date'])


def chart(fig, height=340, ylabel=None):
    fig.update_layout(height=height, margin=dict(l=23, r=23, t=52, b=28), font=dict(family='DM Sans, Arial', color='#7e91a1', size=11), paper_bgcolor='white', plot_bgcolor='white', legend=dict(orientation='h', y=1.14, x=0, font=dict(size=10), bgcolor='rgba(0,0,0,0)'), hovermode='x unified', hoverlabel=dict(bgcolor='#203f56',font_color='white',bordercolor='#203f56'), hoverdistance=50)
    fig.update_xaxes(showgrid=False, zeroline=False)
    fig.update_yaxes(gridcolor='#ecf1f5', griddash='dot', zeroline=False, title=ylabel)
    st.plotly_chart(fig, width='stretch', config={'displayModeBar': False})


@st.cache_data(ttl=1800, show_spinner=False)
def live_forecast(city, local_date):
    return weather_live.fetch_forecast(city, dt.date.fromisoformat(local_date))


def show_live(city, label, t):
    today = weather_live.local_today(city)
    if st.button(t['refresh']):
        live_forecast.clear()
    try:
        result = live_forecast(city, today.isoformat())
    except (OSError, ValueError, KeyError, TypeError, TimeoutError):
        st.error(t['live_error'])
        return
    forecast = result['daily']
    current = result['current']
    tomorrow = forecast.iloc[1]
    left, right = st.columns([1.4, 1], gap='large')
    with left:
        st.markdown(hero_markup(t['tomorrow'], tomorrow['temperature_2m_mean'], tomorrow['date'], label, f"{t['low']}: {tomorrow['temperature_2m_min']:.1f} °C   /   {t['high']}: {tomorrow['temperature_2m_max']:.1f} °C"), unsafe_allow_html=True)
    with right:
        a,b = st.columns(2)
        a.metric(t['now'], f'{current["temperature_2m"]:.1f} °C')
        b.metric(t['feels'], f'{current["apparent_temperature"]:.1f} °C')
        a.metric(t['humidity'], f'{current["relative_humidity_2m"]:.0f}%')
        b.metric(t['wind'], f'{current["wind_speed_10m"]:.1f} km/h')
    st.caption(t['current_time'] + ': ' + current['time'].replace('T',' ') + ' · ' + result['timezone'])
    st.subheader(t['week'])
    st.markdown(forecast_strip(forecast, t['rain_chance']), unsafe_allow_html=True)
    st.caption(t['mean'] + ' · °C / ' + t['low'] + ' / ' + t['high'] + ' · ' + t['rain_chance'])
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=forecast['date'],y=forecast['temperature_2m_max'],name=t['high'],line=dict(color='#e7b259',width=2)))
    fig.add_trace(go.Scatter(x=forecast['date'],y=forecast['temperature_2m_min'],name=t['low'],line=dict(color='#9dc8e6',width=2),fill='tonexty',fillcolor='rgba(58,131,198,.07)'))
    fig.add_trace(go.Scatter(x=forecast['date'],y=forecast['temperature_2m_mean'],name=t['mean'],mode='lines+markers',line=dict(color='#3a83c6',width=3)))
    chart(fig,350,'°C')
    shown = forecast.rename(columns={'date':t['date'],'temperature_2m_mean':t['mean']+' °C','temperature_2m_min':t['low']+' °C','temperature_2m_max':t['high']+' °C','precipitation_sum':t['rain']+' mm','precipitation_probability_max':t['rain_chance']+' %','wind_speed_10m_max':t['wind']+' km/h'}).copy()
    shown[t['date']] = shown[t['date']].dt.strftime('%d.%m.%Y')
    st.dataframe(shown,hide_index=True,width='stretch')
    st.caption(t['retrieved'] + ': ' + pd.Timestamp(result['fetched_at_utc']).tz_convert(result['timezone']).strftime('%d.%m.%Y %H:%M %Z'))
    st.info(t['live_source'])
    st.markdown('[Open-Meteo](https://open-meteo.com/) · [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)')


def main():
    with st.sidebar:
        st.markdown(f'<div class="brand"><span class="brand-icon">{BRAND_ICON}</span>SkyCast</div><div class="brand-sub">WEATHER & MODEL INTELLIGENCE</div>', unsafe_allow_html=True)
        language = st.selectbox('Language / Sprache / Dil', ['English', 'Deutsch', 'Türkçe'])
        lang = {'English': 'en', 'Deutsch': 'de', 'Türkçe': 'tr'}[language]
        t = TEXT[lang]
        city = st.selectbox(t['city'], list(CITIES), format_func=lambda c: CITY_LABELS[lang][list(CITIES).index(c)])
        page = st.radio(t['view'], ['live', 'overview', 'lab', 'validation'], format_func=lambda v: t[v], label_visibility='collapsed', key='skycast_view')
        st.markdown('---')
        st.caption('52.23° N · 21.01° E' if city == 'warsaw' else f"{CITIES[city]['latitude']:.2f}° / {CITIES[city]['longitude']:.2f}°")
        st.caption('Live + ML research · Open-Meteo')
        st.caption('Cenker Sule · AI & Data Science')
    models, report = resources()
    city_report = report['cities'][city]
    model = models[city]
    daily = load_city(city)
    test = predictions().query('city == @city').copy()
    label = CITY_LABELS[lang][list(CITIES).index(city)]
    st.markdown(f'<div class="kicker"><b>SKYCAST</b> / {t["tag"]}<span>{t["live"] if page == "live" else t["edition"]}</span></div>', unsafe_allow_html=True)
    st.title(label + ' / ' + t[page])
    st.markdown(f'<div class="sub">{t["live_intro"] if page == "live" else t["intro"] if page == "overview" else t["lab_intro"] if page == "lab" else t["method_intro"]}</div>', unsafe_allow_html=True)
    if page == 'live':
        show_live(city, label, t)
    elif page == 'overview':
        st.caption(t['replay'])
        date = st.date_input(t['date'], value=dt.date(2025, 7, 15), min_value=dt.date(2024, 1, 1), max_value=dt.date(2025, 12, 31))
        row = test.loc[test['date'].eq(pd.Timestamp(date))].iloc[0]
        hero, info = st.columns([1.4, 1], gap='large')
        with hero:
            st.markdown(hero_markup(t['target'], row['prediction'], date, label, f"{t['asof']}: {date-dt.timedelta(days=1):%d.%m.%Y}"), unsafe_allow_html=True)
        with info:
            a, b = st.columns(2)
            a.metric(t['actual'], f'{row["actual"]:.1f} °C')
            b.metric(t['mae'], f'{city_report["test_metrics"][model["name"]]["mae"]:.2f} °C')
            st.markdown(f'**{t["interval"]}:** {row["lower"]:.1f} — {row["upper"]:.1f} °C')
            st.caption(f'{t["coverage"]}: {city_report["test_interval_coverage"]:.1%} · {t["model"]}: {model["name"]}')
        st.write('')
        left, right = st.columns([1.75, 1], gap='large')
        with left:
            st.subheader(t['timeline'])
            window = test.loc[test['date'].between(pd.Timestamp(date)-pd.Timedelta(days=14), pd.Timestamp(date)+pd.Timedelta(days=14))]
            fig = go.Figure()
            fig.add_trace(go.Scatter(x=window['date'], y=window['upper'], line=dict(width=0), showlegend=False, hoverinfo='skip'))
            fig.add_trace(go.Scatter(x=window['date'], y=window['lower'], line=dict(width=0), fill='tonexty', fillcolor='rgba(58,131,198,.09)', name=t['band'], hoverinfo='skip'))
            fig.add_trace(go.Scatter(x=window['date'], y=window['actual'], name=t['observed'], line=dict(color='#273e50', width=2.4)))
            fig.add_trace(go.Scatter(x=window['date'], y=window['prediction'], name=t['predicted'], line=dict(color='#438fc8', width=2.4)))
            fig.add_vline(x=pd.Timestamp(date).timestamp()*1000, line=dict(color='#e5b156', dash='dot'))
            chart(fig, ylabel='°C')
            st.caption(t['timeline_note'])
        with right:
            st.subheader(t['season'])
            train = daily.loc[daily['date'].dt.year <= 2020]
            seasonal = train.groupby(train['date'].dt.month)['temperature_2m_mean'].mean()
            months = {'en': ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'], 'de':['Jan','Feb','Mär','Apr','Mai','Jun','Jul','Aug','Sep','Okt','Nov','Dez'], 'tr':['Oca','Şub','Mar','Nis','May','Haz','Tem','Ağu','Eyl','Eki','Kas','Ara']}[lang]
            fig = go.Figure(go.Bar(x=months, y=seasonal, marker=dict(color=['#d1e3ef' if v < 15 else '#edc47a' for v in seasonal], cornerradius=4)))
            chart(fig, ylabel='°C')
            st.caption(t['season_note'])
        st.info(t['limits'])
    elif page == 'lab':
        history = daily.tail(30).copy()
        st.download_button(t['download'], history.to_csv(index=False), file_name=f'{city}_history.csv', mime='text/csv')
        st.caption(t['history_note'])
        upload = st.file_uploader(t['upload'], type=['csv'])
        if upload is not None:
            try:
                history = validate_daily(pd.read_csv(upload))
            except (ValueError, TypeError, OverflowError, pd.errors.ParserError, UnicodeDecodeError) as error:
                st.error(t['input_error'] + ': ' + str(error))
                return
        else:
            st.caption(t['lab_note'])
        train = daily.loc[daily['date'].dt.year <= 2020]
        if ((history[WEATHER] < train[WEATHER].min()) | (history[WEATHER] > train[WEATHER].max())).any().any():
            st.warning(t['outside'])
        x = next_features(history)
        estimate = float(predict(model, x)[0])
        next_date = x.index[0]
        a, b, c = st.columns(3)
        a.metric(t['result'], f'{estimate:.1f} °C')
        b.metric(t['lab_date'], next_date.strftime('%d.%m.%Y'))
        radius = model['interval_radius']
        c.metric(t['interval'], f'{estimate-radius:.1f} — {estimate+radius:.1f} °C')
        st.caption(t['asof'] + ': ' + history['date'].iloc[-1].strftime('%d.%m.%Y'))
        st.subheader(t['history'])
        fig = go.Figure(go.Scatter(x=history['date'], y=history['temperature_2m_mean'], name=t['observed'], line=dict(color='#3a83c6', width=2.5)))
        fig.add_trace(go.Scatter(x=[next_date], y=[estimate], mode='markers', name=t['predicted'], marker=dict(color='#e7b259', size=12), error_y=dict(type='data', array=[radius], color='#e7b259')))
        chart(fig, 350, '°C')
        with st.expander(t['history']):
            st.dataframe(history, hide_index=True, width='stretch')
        st.info(t['caution'])
    else:
        a, b, c = st.columns(3)
        selected_metrics = city_report['test_metrics'][model['name']]
        persistence = city_report['test_metrics']['Persistence']['mae']
        a.metric(t['mae'], f'{selected_metrics["mae"]:.2f} °C')
        b.metric(t['gain'], f'{100*(1-selected_metrics["mae"]/persistence):.1f}%')
        c.metric(t['coverage'], f'{city_report["test_interval_coverage"]:.1%}')
        left, right = st.columns([1.2, 1], gap='large')
        with left:
            st.subheader(t['comparison'])
            rows = [{t['model_label']: name, 'MAE (°C)': m['mae'], 'RMSE (°C)': m['rmse'], 'Bias (°C)': m['bias']} for name,m in city_report['test_metrics'].items()]
            st.dataframe(pd.DataFrame(rows).round(3), hide_index=True, width='stretch')
            st.caption(t['model'] + ': ' + model['name'])
        with right:
            st.subheader(t['months'])
            monthly = test.assign(error=(test['prediction']-test['actual']).abs()).groupby(test['date'].dt.month)['error'].mean()
            chart(go.Figure(go.Bar(x=monthly.index, y=monthly, marker=dict(color='#87b2d0', cornerradius=4))), 260, 'MAE °C')
        st.subheader(t['split'])
        split_labels = {'train': t['training'], 'validation': t['selection'], 'calibration': t['calibration'], 'test': t['test']}
        st.dataframe(pd.DataFrame([{t['partition']: split_labels[k], t['rows']: v['rows'], t['period']: v['start'] + ' → ' + v['end']} for k,v in city_report['splits'].items()]), hide_index=True, width='stretch')
        st.info(t['caution'])
        st.subheader(t['city_compare'])
        rows = []
        for key, r in report['cities'].items():
            mae = r['test_metrics'][r['selected_model']]['mae']
            base = r['test_metrics']['Persistence']['mae']
            rows.append({t['city']: CITY_LABELS[lang][list(CITIES).index(key)], t['model_label']: r['selected_model'], 'MAE (°C)': round(mae,3), t['gain']: f'{1-mae/base:.1%}', t['coverage']: f'{r["test_interval_coverage"]:.1%}'})
        st.dataframe(pd.DataFrame(rows), hide_index=True, width='stretch')
        st.download_button(t['table'], test.to_csv(index=False), file_name=f'{city}_test_predictions.csv', mime='text/csv')
    with st.expander(t['details']):
        st.write(t['detail_text'])
        st.markdown('[Open-Meteo / ERA5](https://open-meteo.com/en/docs/historical-weather-api) · [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)')
    st.markdown(f'<div class="footer">{t["live_foot"] if page == "live" else t["foot"]}</div>', unsafe_allow_html=True)


if __name__ == '__main__':
    main()
