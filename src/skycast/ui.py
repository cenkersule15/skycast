TEXT = {
    'en': {
        'tag': 'WEATHER INTELLIGENCE', 'edition': 'RESEARCH EDITION', 'city': 'Choose a city', 'language': 'Language / Sprache / Dil',
        'overview': 'Forecast overview', 'lab': 'Next-day lab', 'validation': 'Model validation', 'replay': 'HISTORICAL REPLAY · 2024–2025',
        'subtitle': 'Tomorrow’s temperature. A model you can inspect.', 'intro': 'Explore one-day-ahead temperature predictions across eight cities, built from historical weather.',
        'date': 'Forecast date', 'asof': 'Complete input data through', 'target': 'Predicted daily mean', 'actual': 'Actual reanalysis mean', 'mae': 'Test MAE', 'gain': 'Improvement over persistence',
        'interval': '90% calibration band', 'coverage': 'Observed test coverage', 'timeline': 'Forecast vs. reality', 'timeline_note': 'Each prediction uses only weather from earlier days. The model stays fixed throughout the test period.',
        'observed': 'Reanalysis', 'predicted': 'SkyCast', 'baseline': 'Yesterday = tomorrow', 'season': 'The seasonal picture', 'season_note': 'Monthly mean temperatures · training years 2010–2020',
        'foot': 'ERA5 reanalysis via Open-Meteo · temperatures in °C · Cenker Sule', 'limits': 'Retrospective research demo. ERA5 is delayed reanalysis, not a live station feed. These results do not establish real-time forecasting accuracy.',
        'lab_intro': 'Use at least 14 consecutive complete days for the selected city. SkyCast predicts the following local calendar day. No live weather API is called.',
        'download': 'Download example history', 'upload': 'Upload daily weather CSV', 'history': 'Input history', 'source': 'Bundled history', 'result': 'Next-day estimate',
        'lab_date': 'Prediction date', 'lab_note': 'Bundled example ends on 31 December 2025. Its next day is 1 January 2026, not the current date.',
        'table': 'Download test predictions', 'method': 'Chronological evaluation', 'method_intro': 'Fit on 2010–2020, select the model on 2021–2022, calibrate interval width on 2023, evaluate once on 2024–2025.',
        'comparison': 'Benchmark comparison', 'city_compare': 'Across the cities', 'split': 'Data partitions', 'months': 'Error by month', 'error': 'Mean absolute error (°C)',
        'caution': 'The calibration band uses the 90th percentile of absolute 2023 residuals. Temporal dependence and drift mean 90% future coverage is not guaranteed.',
        'model': 'Selected model', 'rows': 'Days', 'period': 'Period', 'partition': 'Partition', 'training': 'Training', 'selection': 'Validation', 'calibration': 'Calibration', 'test': 'Test',
        'outside': 'Some inputs fall outside the training range. Predictions and bands may be unreliable.', 'input_error': 'Could not read this history', 'details': 'Data source and scope',
        'detail_text': 'Daily mean, minimum and maximum temperature, precipitation, wind and solar radiation at fixed city coordinates. ERA5 represents a grid cell, not every neighbourhood. The model uses 17 features from completed days and the target date.',
        'unit': 'Daily mean temperature (°C)', 'model_label': 'Model', 'band': 'Calibration band', 'view': 'View', 'history_note': 'Columns: date; temperatures in °C; precipitation in mm; wind in km/h; radiation in MJ/m².',
    },
    'de': {
        'tag': 'WETTER INTELLIGENCE', 'edition': 'FORSCHUNGSDEMO', 'city': 'Stadt auswählen', 'language': 'Language / Sprache / Dil',
        'overview': 'Prognoseübersicht', 'lab': 'Folgetag-Labor', 'validation': 'Modellvalidierung', 'replay': 'HISTORISCHE AUSWERTUNG · 2024–2025',
        'subtitle': 'Die Temperatur von morgen. Nachvollziehbar modelliert.', 'intro': 'Eintägige Temperaturprognosen für acht Städte auf Basis historischer Wetterdaten.',
        'date': 'Prognosedatum', 'asof': 'Vollständige Eingabedaten bis', 'target': 'Prognostiziertes Tagesmittel', 'actual': 'Tatsächliches Reanalyse-Mittel', 'mae': 'Test-MAE', 'gain': 'Verbesserung zur Persistenz',
        'interval': '90-%-Kalibrierungsband', 'coverage': 'Beobachtete Testabdeckung', 'timeline': 'Prognose und Wirklichkeit', 'timeline_note': 'Jede Prognose verwendet nur Wetterdaten früherer Tage. Das Modell bleibt im Testzeitraum unverändert.',
        'observed': 'Reanalyse', 'predicted': 'SkyCast', 'baseline': 'Morgen wie gestern', 'season': 'Der Jahresverlauf', 'season_note': 'Monatsmittel · Trainingsjahre 2010–2020',
        'foot': 'ERA5-Reanalyse über Open-Meteo · Temperaturen in °C · Cenker Sule', 'limits': 'Retrospektive Forschungsdemo. ERA5 ist verzögerte Reanalyse, kein Live-Messnetz. Die Ergebnisse belegen keine Echtzeit-Prognosegüte.',
        'lab_intro': 'Mindestens 14 aufeinanderfolgende vollständige Tage für die gewählte Stadt. SkyCast prognostiziert den folgenden lokalen Kalendertag. Keine Live-Wetter-API.',
        'download': 'Beispielverlauf herunterladen', 'upload': 'Tägliche Wetterdaten als CSV hochladen', 'history': 'Eingabeverlauf', 'source': 'Mitgelieferter Verlauf', 'result': 'Schätzung für den Folgetag',
        'lab_date': 'Prognosedatum', 'lab_note': 'Das Beispiel endet am 31. Dezember 2025. Der Folgetag ist der 1. Januar 2026, nicht das aktuelle Datum.',
        'table': 'Testprognosen herunterladen', 'method': 'Zeitlich geordnete Auswertung', 'method_intro': 'Training: 2010–2020. Modellauswahl: 2021–2022. Intervallkalibrierung: 2023. Unabhängiger Test: 2024–2025.',
        'comparison': 'Modellvergleich', 'city_compare': 'Städte im Vergleich', 'split': 'Datenaufteilung', 'months': 'Fehler nach Monat', 'error': 'Mittlerer absoluter Fehler (°C)',
        'caution': 'Das Band basiert auf dem 90. Perzentil absoluter Residuen aus 2023. Zeitliche Abhängigkeiten und Drift erlauben keine Garantie für 90 % künftige Abdeckung.',
        'model': 'Gewähltes Modell', 'rows': 'Tage', 'period': 'Zeitraum', 'partition': 'Partition', 'training': 'Training', 'selection': 'Validierung', 'calibration': 'Kalibrierung', 'test': 'Test',
        'outside': 'Einige Eingaben liegen außerhalb des Trainingsbereichs. Prognosen und Bänder können unzuverlässig sein.', 'input_error': 'Verlauf konnte nicht gelesen werden', 'details': 'Datenquelle und Geltungsbereich',
        'detail_text': 'Tägliche mittlere, minimale und maximale Temperatur, Niederschlag, Wind und Solarstrahlung an festen Stadtkoordinaten. ERA5 beschreibt eine Rasterzelle. Das Modell nutzt 17 Merkmale aus abgeschlossenen Tagen und dem Zieldatum.',
        'unit': 'Tagesmitteltemperatur (°C)', 'model_label': 'Modell', 'band': 'Kalibrierungsband', 'view': 'Ansicht', 'history_note': 'Spalten: date; Temperaturen in °C; Niederschlag in mm; Wind in km/h; Strahlung in MJ/m².',
    },
    'tr': {
        'tag': 'HAVA DURUMU ANALİTİĞİ', 'edition': 'ARAŞTIRMA DEMOSU', 'city': 'Şehir seç', 'language': 'Language / Sprache / Dil',
        'overview': 'Tahmin özeti', 'lab': 'Ertesi gün laboratuvarı', 'validation': 'Model değerlendirmesi', 'replay': 'GEÇMİŞ VERİYLE TEST · 2024–2025',
        'subtitle': 'Yarının sıcaklığı. İncelenebilir bir model.', 'intro': 'Sekiz şehir için geçmiş hava verileriyle bir gün sonrası sıcaklık tahminlerini keşfet.',
        'date': 'Tahmin tarihi', 'asof': 'Tamamlanmış girdi verisinin son günü', 'target': 'Tahmini günlük ortalama', 'actual': 'Gerçekleşen reanaliz ortalaması', 'mae': 'Test MAE', 'gain': 'Sabit sıcaklık yaklaşımına göre iyileşme',
        'interval': '%90 kalibrasyon bandı', 'coverage': 'Testte gözlenen kapsama', 'timeline': 'Tahmin ve gerçekleşen değer', 'timeline_note': 'Her tahmin yalnızca önceki günlerin verisini kullanır. Model test dönemi boyunca sabit kalır.',
        'observed': 'Reanaliz', 'predicted': 'SkyCast', 'baseline': 'Yarın = dün', 'season': 'Mevsimsel görünüm', 'season_note': 'Aylık sıcaklık ortalamaları · eğitim yılları 2010–2020',
        'foot': 'Open-Meteo üzerinden ERA5 reanalizi · sıcaklıklar °C · Cenker Sule', 'limits': 'Geçmiş verilerle araştırma demosudur. ERA5 gecikmeli reanalizdir; canlı istasyon verisi değildir. Sonuçlar gerçek zamanlı tahmin başarısını kanıtlamaz.',
        'lab_intro': 'Seçtiğin şehir için en az 14 ardışık tamamlanmış gün kullan. SkyCast sonraki yerel takvim gününü tahmin eder. Canlı hava API’si çağrılmaz.',
        'download': 'Örnek geçmişi indir', 'upload': 'Günlük hava verisini CSV olarak yükle', 'history': 'Girdi geçmişi', 'source': 'Hazır geçmiş verisi', 'result': 'Ertesi gün tahmini',
        'lab_date': 'Tahmin tarihi', 'lab_note': 'Hazır örnek 31 Aralık 2025’te biter. Sonraki gün 1 Ocak 2026’dır; güncel tarih değildir.',
        'table': 'Test tahminlerini indir', 'method': 'Tarih sıralı değerlendirme', 'method_intro': 'Eğitim: 2010–2020. Model seçimi: 2021–2022. Bant kalibrasyonu: 2023. Ayrı test: 2024–2025.',
        'comparison': 'Model karşılaştırması', 'city_compare': 'Şehirler arası karşılaştırma', 'split': 'Veri bölümleri', 'months': 'Aya göre hata', 'error': 'Ortalama mutlak hata (°C)',
        'caution': 'Bant, 2023 mutlak tahmin hatalarının %90 yüzdeliğini kullanır. Zaman bağımlılığı ve veri değişimleri nedeniyle gelecekte %90 kapsama garantisi yoktur.',
        'model': 'Seçilen model', 'rows': 'Gün', 'period': 'Dönem', 'partition': 'Bölüm', 'training': 'Eğitim', 'selection': 'Doğrulama', 'calibration': 'Kalibrasyon', 'test': 'Test',
        'outside': 'Bazı girdiler eğitim aralığının dışında. Tahmin ve bantlar güvenilir olmayabilir.', 'input_error': 'Geçmiş verisi okunamadı', 'details': 'Veri kaynağı ve kapsam',
        'detail_text': 'Sabit şehir koordinatlarında günlük ortalama, en düşük ve en yüksek sıcaklık, yağış, rüzgâr ve güneş ışınımı. ERA5 her mahalleyi değil bir ızgara hücresini temsil eder. Model tamamlanmış günlerden ve hedef tarihten 17 özellik kullanır.',
        'unit': 'Günlük ortalama sıcaklık (°C)', 'model_label': 'Model', 'band': 'Kalibrasyon bandı', 'view': 'Görünüm', 'history_note': 'Sütunlar: date; sıcaklık °C; yağış mm; rüzgâr km/sa; ışınım MJ/m².',
    },
}
CITY_LABELS = {
    'en': ['Warsaw', 'Istanbul', 'Berlin', 'Paris', 'London', 'Rome', 'Madrid', 'Ankara'],
    'de': ['Warschau', 'Istanbul', 'Berlin', 'Paris', 'London', 'Rom', 'Madrid', 'Ankara'],
    'tr': ['Varşova', 'İstanbul', 'Berlin', 'Paris', 'Londra', 'Roma', 'Madrid', 'Ankara'],
}

LIVE_TEXT = {
'en': {'live':'Live weather','live_intro':'Current weather estimates and the next seven days for your selected city.','refresh':'Refresh forecast','live_source':'Source: Open-Meteo Forecast API. Live values come from weather models, not the SkyCast research model or direct station measurements. Historical ML test scores do not apply to these forecasts.','live_error':'Live forecast is unavailable. Check your internet connection and try refreshing. Historical research views remain available.','tomorrow':'Tomorrow · daily mean','now':'Current model estimate','feels':'Feels like','humidity':'Humidity','wind':'Wind','week':'The next seven days','low':'Minimum','high':'Maximum','mean':'Daily mean','rain':'Precipitation','rain_chance':'Rain probability','retrieved':'Retrieved','current_time':'Provider time','live_foot':'Live: Open-Meteo Forecast API · Research: ERA5 · Cenker Sule'},
'de': {'live':'Aktuelles Wetter','live_intro':'Aktuelle Wetterschätzungen und die nächsten sieben Tage für die gewählte Stadt.','refresh':'Prognose aktualisieren','live_source':'Quelle: Open-Meteo Forecast API. Aktuelle Werte stammen aus Wettermodellen, nicht aus dem SkyCast-Forschungsmodell oder direkten Stationsmessungen. Historische ML-Testmetriken gelten nicht für diese Prognosen.','live_error':'Aktuelle Prognose nicht verfügbar. Internetverbindung prüfen und erneut aktualisieren. Historische Forschungsansichten bleiben verfügbar.','tomorrow':'Morgen · Tagesmittel','now':'Aktuelle Modellschätzung','feels':'Gefühlt','humidity':'Luftfeuchtigkeit','wind':'Wind','week':'Die nächsten sieben Tage','low':'Minimum','high':'Maximum','mean':'Tagesmittel','rain':'Niederschlag','rain_chance':'Regenwahrscheinlichkeit','retrieved':'Abgerufen','current_time':'Anbieterzeit','live_foot':'Aktuell: Open-Meteo Forecast API · Forschung: ERA5 · Cenker Sule'},
'tr': {'live':'Güncel hava durumu','live_intro':'Seçtiğin şehir için güncel hava tahmini ve önümüzdeki yedi gün.','refresh':'Tahmini yenile','live_source':'Kaynak: Open-Meteo Forecast API. Güncel değerler hava modellerinden gelir; SkyCast araştırma modelinin tahmini veya doğrudan istasyon ölçümü değildir. Geçmiş ML test sonuçları bu tahminlere ait değildir.','live_error':'Güncel tahmin alınamadı. İnternet bağlantısını kontrol edip yenile. Geçmiş model ekranlarını kullanmaya devam edebilirsin.','tomorrow':'Yarın · günlük ortalama','now':'Şu anki model tahmini','feels':'Hissedilen','humidity':'Nem','wind':'Rüzgâr','week':'Önümüzdeki yedi gün','low':'En düşük','high':'En yüksek','mean':'Günlük ortalama','rain':'Yağış','rain_chance':'Yağış olasılığı','retrieved':'Alınma zamanı','current_time':'Sağlayıcı zamanı','live_foot':'Güncel: Open-Meteo Forecast API · Araştırma: ERA5 · Cenker Sule'},
}
for language, values in LIVE_TEXT.items():
    TEXT[language].update(values)
TEXT['en']['overview'] = 'Historical ML replay'
TEXT['de']['overview'] = 'Historischer ML-Test'
TEXT['tr']['overview'] = 'Geçmiş ML testi'

CSS = r'''
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Manrope:wght@400;500;600;700;800&display=swap');
:root { --ink:#172d42; --muted:#7a8998; --blue:#4c8cb7; --line:#e0e7ed; }
.stApp { background:radial-gradient(ellipse at 95% 0%,#e8eff5 0,transparent 45%),#f5f7f9; color:var(--ink); font-family:'DM Sans',-apple-system,BlinkMacSystemFont,sans-serif; }
h1,h2,h3,[data-testid="stMetricValue"] { font-family:'Manrope',-apple-system,sans-serif !important; }
[data-testid="stHeader"] { background:rgba(245,247,249,.95); border-bottom:1px solid #e2e8ee70; }
[data-testid="stMainBlockContainer"] { padding:4.9rem 3.5rem 2rem; max-width:1500px; }
[data-testid="stSidebar"] { background:linear-gradient(180deg,#fcfdfe,#f0f4f7); border-right:1px solid #dce5ed; }
[data-testid="stSidebar"] > div:first-child { padding-top:2.6rem; }
[data-testid="stSidebar"] [data-testid="stRadio"] label { padding:11px 12px; border-radius:11px; margin:3px 0; border:1px solid transparent; transition:background .18s; }
[data-testid="stSidebar"] [data-testid="stRadio"] label:hover { background:#e8eff5; }
[data-testid="stSidebar"] [data-testid="stRadio"] label:has(input:checked) { background:#e3edf5; border-color:#cadae7; box-shadow:inset 3px 0 #4b86ae; }
[data-testid="stSidebar"] [data-testid="stCaptionContainer"] { font-size:10px; line-height:1.7; }
[data-baseweb="select"] > div { border-radius:11px; background:#fff; border-color:#d9e3eb; min-height:46px; }
.kicker { color:#8a9aa8; font-size:9px; letter-spacing:2px; font-weight:700; display:flex; justify-content:space-between; align-items:center; gap:12px; padding-bottom:18px; border-bottom:1px solid #dce5ed; margin-bottom:24px; }
.kicker b { color:#385c77; font-weight:700; }
.kicker span { color:#4b7897; font-size:9px; letter-spacing:1px; padding:7px 11px; background:#e7f0f7; border:1px solid #d5e4ef; border-radius:20px; white-space:nowrap; }
h1 { font-size:44px !important; letter-spacing:-1.8px; font-weight:800 !important; padding:0 !important; line-height:1.2!important; }
h3 { font-size:19px !important; letter-spacing:-.5px; font-weight:700 !important; padding-top:20px!important; }
.sub { max-width:800px; color:#7a8996; font-size:13px; line-height:1.8; margin:10px 0 20px; }
.hero { background:radial-gradient(ellipse at 90% 0%,#386c88 0,transparent 57%),linear-gradient(120deg,#162d43,#224a63); color:#fff; padding:28px 30px; border:1px solid #3a5c75; border-radius:21px; position:relative; overflow:hidden; min-height:247px; box-shadow:0 13px 28px #203d5615; isolation:isolate; }
.hero:before { content:''; position:absolute; inset:0; background-image:linear-gradient(#ffffff05 1px,transparent 1px),linear-gradient(90deg,#ffffff05 1px,transparent 1px); background-size:44px 44px; z-index:-1; }
.hero .eyebrow { color:#abc5d7; font-size:9px; letter-spacing:1.8px; font-weight:700; max-width:76%; }
.hero .temp { font:700 73px 'Manrope',sans-serif; letter-spacing:-4px; line-height:1.15; margin:15px 0 13px; }
.hero .unit { font-size:29px; font-weight:400; vertical-align:top; letter-spacing:-1px; display:inline-block; padding-top:12px; color:#b4cedf; }
.hero .when { font-size:12px; color:#c1d3df; margin-bottom:16px; }
.hero .hero-detail { display:inline-block; background:#ffffff09; border:1px solid #ffffff15; border-radius:7px; padding:8px 11px; font-size:11px; color:#d4e3ec; max-width:100%; }
.hero .atmosphere { position:absolute; width:210px; height:210px; right:-23px; top:18px; pointer-events:none; z-index:-1; opacity:.85; }
.hero .orb { position:absolute; width:104px; height:104px; right:57px; top:31px; border-radius:50%; background:radial-gradient(circle at 32% 22%,#f5d7a0,#d8ad67 60%,#b88649); box-shadow:0 0 48px #f1cd8d16; }
.hero .orbit { position:absolute; width:180px; height:180px; right:20px; top:-6px; border:1px solid #cfe2ef18; border-radius:50%; }
.hero .orbit.two { width:242px; height:242px; top:-37px; right:-11px; border-style:dashed; border-color:#cfe2ef12; }
.hero .arc { position:absolute; width:310px; height:125px; bottom:-9px; right:-22px; border:1px solid #b9d6e620; border-radius:50%; transform:rotate(-18deg); background:linear-gradient(0deg,#426f8530,transparent); }
[data-testid="stMetric"] { background:linear-gradient(145deg,#fff,#fafcfd); border:1px solid #dfe7ee; padding:19px 21px; border-radius:16px; min-height:122px; box-shadow:0 4px 14px #203d5603; position:relative; overflow:hidden; }
[data-testid="stMetric"]:after { content:''; width:52px; height:52px; border:1px solid #dfebf530; border-radius:50%; position:absolute; right:-12px; top:-12px; }
[data-testid="stMetricValue"] { font-weight:800; font-size:26px; letter-spacing:-.8px; color:#20394f; padding-top:7px; }
[data-testid="stMetricLabel"] { color:#61798e; font-size:11px; }
[data-testid="stMetricLabel"] p,[data-testid="stMetricLabel"] > div { white-space:normal!important; overflow:visible!important; text-overflow:clip!important; }
[data-testid="stMetricValue"] > div { font-size:inherit!important; white-space:normal!important; overflow:visible!important; text-overflow:clip!important; line-height:1.3; }
[data-testid="stPlotlyChart"] { border:1px solid #dfe7ee; border-radius:18px; overflow:hidden; background:white; box-shadow:0 5px 18px #203d5603; }
[data-testid="stDataFrame"] { border:1px solid #dfe7ee; border-radius:14px; overflow:hidden; }
.stButton button,.stDownloadButton button { border-radius:10px; border:1px solid #cfdfe9; background:#e8f0f6; color:#335e7a; font-weight:600; font-size:12px; padding:9px 16px; transition:background .18s,box-shadow .18s; }
.stButton button:hover,.stDownloadButton button:hover { border-color:#779eb9; background:#dfeaf2; color:#183b57; box-shadow:0 3px 8px #315a7610; }
[data-testid="stFileUploaderDropzone"] { background:#fff; border:1px dashed #b8cddd; border-radius:14px; }
[data-testid="stCaptionContainer"] { color:#6e8293; line-height:1.6; font-size:11px; }
[data-testid="stAlert"] { border-radius:12px; border:1px solid #dfebf3; background:#ebf2f7; font-size:12px; }
[data-testid="stExpander"] { background:#ffffff60; border-radius:12px; }
.brand { display:flex; align-items:center; gap:11px; margin:4px 0 5px; font:800 28px 'Manrope',sans-serif; letter-spacing:-1.5px; color:#1e3b53; }
.brand-icon { display:flex; align-items:center; justify-content:center; width:44px; height:44px; background:linear-gradient(145deg,#203f59,#355f7a); color:#edc98c; border:1px solid #426985; border-radius:14px; box-shadow:0 5px 10px #29496315; }
.brand-icon svg { width:27px; height:27px; }
.brand-sub { margin:0 0 30px 55px; color:#8399aa; font-size:8px; letter-spacing:1.5px; }
.week-strip { display:grid; grid-template-columns:repeat(7,minmax(0,1fr)); gap:10px; margin:14px 0 8px; }
.day-card { background:#ffffffb0; border:1px solid #dfe7ee; border-radius:14px; padding:16px 12px; text-align:center; }
.day-card.focus { background:#eaf1f7; border-color:#c1d5e4; }
.day-date { color:#8395a4; font-size:10px; letter-spacing:.3px; }
.day-value { color:#2e536c; font:800 23px 'Manrope',sans-serif; letter-spacing:-1px; margin:9px 0 5px; }
.day-range { color:#8b9caa; font-size:10px; white-space:nowrap; }
.day-rain { color:#779db8; font-size:10px; margin-top:12px; display:flex; align-items:center; justify-content:center; gap:5px; }
.day-rain svg {width:10px;height:12px;}
.footer { border-top:1px solid #dce5ed; color:#8e9da9; font-size:10px; margin-top:30px; padding-top:18px; letter-spacing:.2px; }
@media(max-width:1100px) { [data-testid="stMainBlockContainer"]{padding-left:2rem;padding-right:2rem}.hero .atmosphere{right:-65px;opacity:.5}.hero .temp{font-size:64px}.day-card{padding:14px 7px}.day-value{font-size:20px} }
@media(max-width:760px) { [data-testid="stMainBlockContainer"]{padding:4.9rem 1rem 2rem}h1{font-size:32px!important}.week-strip{grid-template-columns:repeat(4,minmax(0,1fr))}.hero{min-height:235px}.hero .atmosphere{right:-10px}.kicker{font-size:8px;letter-spacing:1px}.kicker span{font-size:8px} }
@media(prefers-reduced-motion:reduce) { * {transition:none!important;animation:none!important;} }
</style>
'''

BRAND_ICON = '<svg viewBox="0 0 32 32" fill="none" aria-hidden="true"><circle cx="20" cy="11" r="6" stroke="currentColor" stroke-width="1.5"/><path d="M7 24h16a5 5 0 0 0 0-10h-1a7 7 0 0 0-13-1 5.5 5.5 0 0 0-2 11Z" fill="#294c65" stroke="#c9dce9" stroke-width="1.5"/></svg>'


def hero_markup(eyebrow, temperature, date, city, detail):
    from html import escape
    return f'<div class="hero"><div class="eyebrow">{escape(eyebrow.upper())}</div><div class="temp">{temperature:.1f}<span class="unit"> °C</span></div><div class="when">{date:%d.%m.%Y} · {escape(city)}</div><div class="hero-detail">{escape(detail)}</div><div class="atmosphere" aria-hidden="true"><div class="orbit two"></div><div class="orbit"></div><div class="orb"></div><div class="arc"></div></div></div>'


def forecast_strip(forecast, rain_label):
    cards = []
    drop = '<svg viewBox="0 0 12 16" fill="none" aria-hidden="true"><path d="M6 1S1 7 1 10a5 5 0 0 0 10 0C11 7 6 1 6 1Z" stroke="currentColor" stroke-width="1.4"/></svg>'
    for index, row in forecast.iterrows():
        focus = ' focus' if index == 1 else ''
        cards.append(f'<div class="day-card{focus}"><div class="day-date">{row["date"]:%d.%m}</div><div class="day-value">{row["temperature_2m_mean"]:.1f}°</div><div class="day-range">{row["temperature_2m_min"]:.0f}° / {row["temperature_2m_max"]:.0f}°</div><div class="day-rain" title="{rain_label}">{drop}{row["precipitation_probability_max"]:.0f}%</div></div>')
    return '<div class="week-strip">' + ''.join(cards) + '</div>'
