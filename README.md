# SkyCast · Next-Day Temperature Lab

**Deutsch** | [English](README.en.md) | [Türkçe](README.tr.md)

Ein reproduzierbares Machine-Learning-Projekt für eintägige Temperaturprognosen in **acht Städten**: Warschau, Istanbul, Berlin, Paris, London, Rom, Madrid und Ankara.

**Autor:** Cenker Sule · Artificial Intelligence & Data Science

## Aktuelle Wetterprognosen

Die Startansicht zeigt aktuelle modellbasierte Wetterwerte und eine **7-Tage-Prognose** über die Open-Meteo Forecast API für alle acht Städte. Sie verwendet die lokale Stadtzeit, lädt Daten höchstens 30 Minuten aus dem Cache und bietet eine Schaltfläche zum Aktualisieren. Für diese Ansicht ist Internet erforderlich; bei einem API-Fehler wird keine alte historische Prognose als aktuelle ausgegeben.

Die Ansichten **Historischer ML-Test**, Folgetag-Labor und Modellvalidierung bleiben separat. Die Live-Prognosen stammen vom Wetteranbieter; sie sind keine Ausgabe der eigenen Ridge-/Gradient-Boosting-Modelle. Die untenstehenden Metriken beziehen sich ausschließlich auf den historischen ML-Test.

[Open-Meteo Forecast API](https://open-meteo.com/en/docs) · [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)


## In einer Minute starten

Docker Desktop starten, dann im Projektordner:

```bash
docker compose up --build
```

[http://localhost:8502](http://localhost:8502) öffnen. Der Port ist absichtlich 8502, damit CreditLens auf 8501 parallel weiterlaufen kann. Daten und trainierte Modelle sind enthalten; nur der erste Docker-Build benötigt Internet. Zum Stoppen: `Ctrl+C`, danach `docker compose down`.

## Was die Anwendung zeigt

- Historische Prognosen mit tatsächlichen ERA5-Tagesmitteln und Kalibrierungsband.
- Eigene CSV-Verläufe für eine Prognose des folgenden lokalen Kalendertags.
- Städtevergleich, Saisonverlauf, MAE/RMSE und monatliche Fehler.
- Vergleich von Ridge Regression, Gradient Boosting, Persistenz und saisonalem Mittel.
- Deutsche, englische und türkische Oberfläche; Englisch ist voreingestellt.
- Zeitlich geordnete Auswertung, Eingabeprüfung, automatisierte Tests und Docker.

## Gemessene Ergebnisse

Unabhängiger Test: **2024–2025, 731 Tage pro Stadt**, insgesamt **5.848 Prognosen**. Modellwahl ausschließlich anhand der Validierungs-MAE 2021–2022. Persistenz setzt den Wert des letzten vollständigen Tages als Prognose für den Folgetag ein. Kleinere MAE ist besser.

| Stadt | Gewähltes Modell | MAE °C | Persistenz-MAE °C | Verbesserung | Bandabdeckung im Test |
| --- | --- | ---: | ---: | ---: | ---: |
| Warsaw | Gradient boosting | 1.553 | 1.712 | 9.3% | 91.9% |
| Istanbul | Gradient boosting | 0.815 | 0.957 | 14.8% | 94.5% |
| Berlin | Gradient boosting | 1.538 | 1.766 | 12.9% | 90.6% |
| Paris | Gradient boosting | 1.460 | 1.679 | 13.1% | 86.6% |
| London | Ridge regression | 1.378 | 1.571 | 12.3% | 89.7% |
| Rome | Gradient boosting | 1.004 | 1.085 | 7.5% | 91.2% |
| Madrid | Gradient boosting | 1.176 | 1.381 | 14.9% | 88.6% |
| Ankara | Gradient boosting | 1.159 | 1.408 | 17.7% | 89.2% |

Die Verbesserung bezieht sich auf die Persistenzreferenz, nicht auf professionelle Wetterdienste. Die Modelle werden pro Stadt gewählt; London verwendet Ridge, die übrigen Städte Gradient Boosting.

## Methodik

| Zeitraum | Verwendung |
| --- | --- |
| 2010–2020 | Modelltraining; nach 14 Tagen Anlauf verbleiben 4.004 Beispiele pro Stadt |
| 2021–2022 | Modellauswahl anhand der MAE, 730 Beispiele |
| 2023 | Kalibrierung der Intervallbreite, 365 Beispiele |
| 2024–2025 | Unabhängiger Test, 731 Beispiele |

Ziel ist das **Tagesmittel der Lufttemperatur in 2 m Höhe**. 17 Merkmale verwenden nur abgeschlossene Tage: vergangene Temperaturen, Niederschlag, Wind, Solarstrahlung, gleitende Mittel, Temperaturänderung und zyklische Merkmale des Zieldatums. Kein zufälliger Split und keine Wetterwerte des Zieltags als Eingabe.

Ridge wird nach Standardisierung auf dem Training angepasst. Gradient Boosting lernt die Temperaturänderung zur Persistenz. Hyperparameter sind fest; die Validierung wählt zwischen den beiden Modellen und Persistenz. Modelle bleiben nach dem Training unverändert. Beim fortlaufenden eintägigen Test stehen die realisierten Wetterdaten früherer Testtage zur Verfügung; dies ist keine mehrtägige rekursive Prognose.

Das symmetrische Band basiert pro Stadt auf dem endlichen Stichprobenquantil der absoluten Kalibrierungsfehler bei Zielabdeckung 90 %. Wegen zeitlicher Abhängigkeit und Drift besteht **keine Garantie für künftige 90-%-Abdeckung**; die Tabelle zeigt die tatsächlich gemessene Abdeckung.

## Datenquelle und Grenzen

**Open-Meteo Historical Weather API**, Modell ausdrücklich `era5`, tägliche Werte vom 01.01.2010 bis 31.12.2025 in der jeweiligen lokalen Zeitzone. Grundlage: ECMWF / Copernicus Climate Change Service ERA5. Die Antwort repräsentiert eine Rasterzelle an festen Stadtkoordinaten, keine individuelle Wetterstation.

[Open-Meteo / ERA5-Dokumentation](https://open-meteo.com/en/docs/historical-weather-api) · [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)

**Der eigene ML-Bereich ist eine retrospektive Forschungsdemo.** ERA5 wird mit Verzögerung veröffentlicht und verwendet nachträgliche Informationen aus Reanalyse. Das Experiment zeigt Modellgüte unter idealisierter Verfügbarkeit früherer Wetterdaten; keine Aussage zur operationellen Echtzeitgüte. Das mitgelieferte CSV-Beispiel endet am 31.12.2025 und prognostiziert entsprechend den 01.01.2026. Temperatur, Niederschlag und andere Zielgrößen außer dem Tagesmittel werden nicht vorhergesagt.

## Python und Reproduzierbarkeit

Python 3.12:

```bash
python3.12 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements-dev.txt
python -m pip install --no-deps -e .
python -m streamlit run app.py --server.port=8502
```

Training aus den enthaltenen Daten und Tests:

```bash
python -m skycast.train
python -m pytest -q
```

Optional Daten erneut abrufen: `python -m skycast.data` lädt fehlende Stadtdateien und verwendet vorhandene CSVs weiter. Für einen vollständigen Neuabruf die acht Stadt-CSVs vorher außerhalb des Projektordners sichern und entfernen. API-Limits und nachträgliche ERA5-Korrekturen sind möglich. `data/provenance.json` enthält URLs, Zeiträume und Hashes; `artifacts/report.json` dokumentiert Datenaufteilung, Modellauswahl und Metriken.

**Validierung:** 28 lokale Tests bestanden: Zukunftsdaten verändern keine früheren Merkmale; Eingabeprüfung; reproduzierte Testmetriken und zeitlich getrennte Partitionen für acht Städte; alle drei Ansichten in drei Sprachen. Der Streamlit-Server wurde separat über den Health-Endpunkt geprüft. Docker und GitHub Actions sind konfiguriert; ein Docker-Build oder GitHub-Lauf wurde in dieser Umgebung nicht ausgeführt.

## Struktur

| Pfad | Zweck |
| --- | --- |
| `app.py` | Interaktive Oberfläche |
| `src/skycast/data.py` | Datenquelle, Städte und CSV-Prüfung |
| `src/skycast/features.py` | Zeitlich korrekte Merkmale |
| `src/skycast/train.py` | Training, Modellauswahl, Bänder und Auswertung |
| `src/skycast/ui.py` | Übersetzungen und Gestaltung |
| `data/` | Tägliche ERA5-Daten und Herkunftsnachweise |
| `artifacts/` | Trainierte Modelle, Bericht und Testprognosen |
| `tests/` | Modell- und Anwendungstests |

Code: MIT. Wetterdaten: CC BY 4.0 mit Quellenangabe wie oben.
