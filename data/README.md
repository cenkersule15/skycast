# Weather data

Eight city files contain 5,844 daily records each, 2010-01-01 through 2025-12-31. Values are ERA5 reanalysis estimates requested from the Open-Meteo Historical Weather API, using each city’s local timezone.

Columns: `date`, `temperature_2m_mean`, `temperature_2m_max`, `temperature_2m_min` (°C), `precipitation_sum` (mm), `wind_speed_10m_max` (km/h), `shortwave_radiation_sum` (MJ/m²).

Attribution: Weather data by Open-Meteo.com, based on ECMWF / Copernicus Climate Change Service ERA5. API data: CC BY 4.0, https://creativecommons.org/licenses/by/4.0/ . Source: https://open-meteo.com/en/docs/historical-weather-api . These are modified selections and CSV conversions of API responses.

`provenance.json` contains exact request URLs and file hashes. `example_history.csv` contains the last 30 Warsaw days and is intended for input-format demonstration. City coordinates are defined in `src/skycast/data.py`; Istanbul is included as a major city, not as a national capital.
