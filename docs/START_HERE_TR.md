# SkyCast - Hızlı başlangıç

1. ZIP'i masaüstüne çıkar. `skycast` klasörünü VS Code ile aç.
2. Docker Desktop açık olsun.
3. Terminalde çalıştır:

```bash
docker compose up --build
```

4. Tarayıcıda http://localhost:8502 aç.
5. Sol menüden Türkçe ve şehir seç. Ana ekran güncel hava tahminini ve sonraki 7 günü gösterir. Geçmiş ML testi ekranında test tarihi seçebilirsin.
6. Ertesi gün laboratuvarında örnek geçmişi indirip CSV olarak tekrar yükleyebilirsin.
7. Model değerlendirmesi ekranında test hatalarını ve şehir karşılaştırmasını incele.

Model eğitmen ve veri indirmen gerekmiyor. İlk Docker kurulumu internet gerektirir.
CreditLens ayrı klasörde ve 8501 portunda kalır; bu proje 8502 kullanır.

Güncel hava durumu ekranı internet üzerinden Open-Meteo tahminini alır. Geçmiş ML testi ve Ertesi gün laboratuvarı ise kendi eğittiğimiz modelleri gösterir. Örnek geçmiş 2025 sonunda biter, onun ertesi günü 1 Ocak 2026'dır. Kendi CSV geçmişini yüklersen onun son tamamlanmış gününden sonraki günü tahmin eder. Veriler istasyon ölçümü değil ERA5 reanalizidir.

Kod MIT lisanslı; hava verisinin kaynağı Open-Meteo / Copernicus ERA5 ve lisansı CC BY 4.0.
