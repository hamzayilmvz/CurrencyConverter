# 💱 Currency Converter (Tkinter + FreeCurrencyAPI)

Bu proje, **Python Tkinter** kullanılarak yapılmış basit bir döviz çevirici uygulamasıdır.  
Kullanıcıdan alınan tutarı, seçilen iki para birimi arasında çevirir.  

---

## 🚀 Özellikler
- Tkinter arayüzü ile kolay kullanım
- Kullanıcıdan geçerli sayı girilmesini kontrol eder
- Aynı para birimi seçildiğinde uyarı verir
- **FreeCurrencyAPI** üzerinden güncel kurları alır

---

## 📦 Gereksinimler
Bu projeyi çalıştırmak için aşağıdaki kütüphanelere ihtiyaç vardır:

```bash
pip install requests
(Tkinter, Python ile birlikte gelir.)

🔑 API Anahtarı

Proje FreeCurrencyAPI
 kullanmaktadır.
Çalıştırmadan önce kendi API anahtarınızı almanız ve aşağıdaki satıra eklemeniz gerekir:

api_key = "BURAYA_KENDİ_API_KEYİNİZİ_YAZIN"

▶️ Çalıştırma

Yukarıdaki dosyayı currency_converter.py olarak kaydedin.

Terminal veya IDE üzerinden çalıştırın:

python currency_converter.py


Açılan arayüzde:

Tutarı girin

Döviz birimlerini seçin

Çevir butonuna basın

📌 Notlar

Kullanılan dövizler: USD, EUR, GBP, TRY, JPY

İnternet bağlantısı olmadan çalışmaz

Yanlış giriş yapıldığında hata mesajı gösterilir
