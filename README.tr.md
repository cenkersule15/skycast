# SkyCast · Ertesi Gün Sıcaklık Tahmini

[Deutsch](README.md) | [English](README.en.md) | **Türkçe**

**Sekiz şehir için bir gün sonrası ortalama sıcaklığı tahmin eden**, tekrar üretilebilir bir makine öğrenmesi projesi: Varşova, İstanbul, Berlin, Paris, Londra, Roma, Madrid ve Ankara.

**Geliştiren:** Cenker Sule · Yapay Zekâ ve Veri Bilimi

## Güncel hava tahminleri

Ana ekran artık sekiz şehir için Open-Meteo Forecast API üzerinden **güncel hava tahminini ve 7 günlük tahminleri** gösterir. Tarihler şehrin yerel saatine göre hesaplanır. Yanıtlar en fazla 30 dakika önbellekte tutulur; Tahmini yenile düğmesiyle tekrar alınabilir. Bu ekran internet gerektirir. API hatasında eski tarihler güncelmiş gibi gösterilmez.

**Geçmiş ML testi**, Ertesi gün laboratuvarı ve Model değerlendirmesi ayrı ekranlardır. Güncel tahminler hava sağlayıcısından gelir; kendi eğittiğimiz Ridge/gradient boosting modellerinin çıktısı değildir. Aşağıdaki başarı metrikleri yalnızca geçmiş ML testine aittir.

[Open-Meteo Forecast API](https://open-meteo.com/en/docs) · [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)


## Hızlı başlangıç

Docker Desktop'ı aç. Proje klasöründe çalıştır:

```bash
docker compose up --build
```

Tarayıcıda [http://localhost:8502](http://localhost:8502) aç. CreditLens 8501 portunda çalışmaya devam edebilir. Veriler ve eğitimli modeller pakete dahildir; yalnızca ilk Docker kurulumu internet gerektirir. Durdurmak için `Ctrl+C`, ardından `docker compose down` kullan.

## Özellikler

- Geçmiş test tarihleri için tahmin, gerçekleşen ERA5 günlük ortalaması ve kalibrasyon bandı.
- CSV geçmişi yükleyerek son tamamlanmış günün ertesi gününü tahmin etme.
- Şehir karşılaştırması, mevsimsellik, MAE/RMSE ve aylık hata analizi.
- Ridge regresyonu ve gradient boosting modellerini sabit sıcaklık ve mevsimsel ortalama yaklaşımlarıyla karşılaştırma.
- Türkçe, İngilizce ve Almanca arayüz; başlangıç dili İngilizcedir.
- Tarih sıralı değerlendirme, girdi doğrulama, otomatik testler ve Docker.

## Ölçülen sonuçlar

Ayrı tutulan test dönemi: **2024–2025, şehir başına 731 gün**, toplam **5.848 tahmin**. Model seçimi yalnızca 2021–2022 doğrulama verisinin MAE değerine göre yapılır. Sabit sıcaklık yaklaşımı, ertesi günün sıcaklığını son tamamlanmış günle aynı kabul eder. Düşük MAE daha iyidir.

| Şehir | Seçilen model | MAE °C | Sabit sıcaklık MAE °C | İyileşme | Testte bant kapsamı |
| --- | --- | ---: | ---: | ---: | ---: |
| Varşova | Gradient boosting | 1.553 | 1.712 | %9.3 | %91.9 |
| İstanbul | Gradient boosting | 0.815 | 0.957 | %14.8 | %94.5 |
| Berlin | Gradient boosting | 1.538 | 1.766 | %12.9 | %90.6 |
| Paris | Gradient boosting | 1.460 | 1.679 | %13.1 | %86.6 |
| Londra | Ridge regresyonu | 1.378 | 1.571 | %12.3 | %89.7 |
| Roma | Gradient boosting | 1.004 | 1.085 | %7.5 | %91.2 |
| Madrid | Gradient boosting | 1.176 | 1.381 | %14.9 | %88.6 |
| Ankara | Gradient boosting | 1.159 | 1.408 | %17.7 | %89.2 |

İyileşme, profesyonel hava servislerine değil sabit sıcaklık referansına göredir. Londra'da Ridge, diğer şehirlerde gradient boosting seçilmiştir.

## Yöntem

| Dönem | Kullanım |
| --- | --- |
| 2010–2020 | Eğitim; ilk 14 günlük geçmiş gereksinimi sonrası şehir başına 4.004 örnek |
| 2021–2022 | MAE ile model seçimi; 730 örnek |
| 2023 | Bant genişliği kalibrasyonu; 365 örnek |
| 2024–2025 | Ayrı test; 731 örnek |

Hedef, **yerden 2 metre yükseklikte günlük ortalama hava sıcaklığıdır**. Toplam 17 özellik; önceki günlerin sıcaklığı, yağış, rüzgâr, güneş ışınımı, hareketli ortalamalar, sıcaklık değişimi ve hedef tarihin döngüsel takvim bilgisinden oluşur. Rastgele veri bölme yapılmaz; hedef günün hava verisi girdi olarak kullanılmaz.

Ridge için standartlaştırma yalnızca eğitim verisinde öğrenilir. Gradient boosting, sabit sıcaklık tahminine göre sıcaklık farkını öğrenir. Hiperparametreler sabittir; doğrulama verisi her şehir için Ridge, gradient boosting veya sabit sıcaklık yaklaşımını seçer. Modeller doğrulama, kalibrasyon veya test verisiyle yeniden eğitilmez. Ardışık bir günlük testlerde, önceki test günlerinin gerçekleşen hava verileri kullanılabilir; bu, birden fazla günü ileriye doğru yinelemeli tahmin değildir.

Simetrik kalibrasyon bandı, her şehir için 2023 mutlak tahmin hatalarından sonlu örneklem yüzdeliğiyle hesaplanır; hedef kapsam %90'dır. Zaman bağımlılığı ve dağılım değişimleri nedeniyle **gelecekte %90 kapsama garantisi yoktur**. Gerçekte gözlenen test kapsamı tabloda gösterilir.

## Veri kaynağı ve sınırlar

**Open-Meteo Historical Weather API**, açıkça seçilen `era5` modeli; her şehrin yerel saat diliminde 1 Ocak 2010–31 Aralık 2025 günlük verileri. Temel kaynak: ECMWF / Copernicus Climate Change Service ERA5. Veriler sabit koordinatlardaki bir ızgara hücresini temsil eder; belirli bir hava istasyonunun doğrudan ölçümü değildir.

[Open-Meteo / ERA5 dokümantasyonu](https://open-meteo.com/en/docs/historical-weather-api) · [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)

**Kendi ML modellerinin bölümü geçmiş verilerle araştırma demosudur.** ERA5 gecikmeli yayımlanır ve sonradan birleştirilen bilgileri kullanır. Deney, önceki hava verilerine ideal erişim varsayar; gerçek zamanlı operasyonel başarıyı kanıtlamaz. Hazır CSV 31 Aralık 2025'te biter; onun ertesi gün tahmini 1 Ocak 2026 içindir. Kendi ML modellerimiz yalnızca günlük ortalama sıcaklığı tahmin eder; yağış ve diğer hava olaylarını tahmin etmez.

## Python ile çalıştırma

Python 3.12:

```bash
python3.12 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements-dev.txt
python -m pip install --no-deps -e .
python -m streamlit run app.py --server.port=8502
```

Paket içindeki verilerle yeniden eğitim ve test:

```bash
python -m skycast.train
python -m pytest -q
```

İsteğe bağlı veri indirme: `python -m skycast.data`, eksik şehir dosyalarını indirir; mevcut CSV'leri yeniden kullanır. Tümünü yenilemek için önce sekiz şehir CSV'sini proje dışında yedekleyip kaldır. API limitleri ve geçmiş ERA5 verilerinde düzeltmeler olabilir. `data/provenance.json` istek adreslerini, tarihleri ve dosya özetlerini; `artifacts/report.json` veri bölümlerini, model seçimlerini ve metrikleri içerir.

**Doğrulama:** 28 yerel test geçti. Gelecek verinin geçmiş özelliklerini değiştirmemesi, hatalı girdiler, sekiz şehrin yeniden hesaplanan test metrikleri ve tarih sıralı bölümleri, ayrıca üç dilde üç ekran kontrol edildi. Streamlit sağlık uç noktası da kontrol edildi. Docker ve GitHub Actions yapılandırıldı; bu ortamda Docker derlemesi veya GitHub Actions çalışması yapılmadı.

## Proje yapısı

| Dosya / klasör | Amaç |
| --- | --- |
| `app.py` | Etkileşimli panel |
| `src/skycast/data.py` | Veri kaynağı, şehirler ve CSV doğrulaması |
| `src/skycast/features.py` | Tarih sırasına uygun özellik üretimi |
| `src/skycast/train.py` | Eğitim, model seçimi, bantlar ve değerlendirme |
| `src/skycast/ui.py` | Çeviriler ve tasarım |
| `data/` | Günlük ERA5 verileri ve kaynak kayıtları |
| `artifacts/` | Eğitimli modeller, rapor ve test tahminleri |
| `tests/` | Model ve uygulama testleri |

Kod MIT lisanslıdır. Hava verisi, yukarıdaki kaynak belirtilerek CC BY 4.0 lisansıyla sunulur.
