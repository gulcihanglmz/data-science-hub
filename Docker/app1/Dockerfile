# 1. TEMEL İMAJ: Ubuntu'yu (20.04) temel alıyoruz.
FROM ubuntu:20.04

# 2. KURULUM VE TEMİZLİK: Python'ı kurar ve kalıntıları silerek katmanı küçültür.
RUN apt-get update && \
    apt-get install -y --no-install-recommends python3 python3-pip && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# 3. ÇALIŞMA DİZİNİ: Konteynerin içinde /app klasörünü oluştur.
WORKDIR /app

# 4. KOPYALAMA: Uygulamanın kendisini (app.py) kopyalar.
# HATA DÜZELTİLDİ: app.py'yi doğru dizininden alıyoruz.
COPY py-app/app.py .

# 5. BAŞLANGIÇ KOMUTU: Uygulamayı python3 ile çalıştırır.
CMD ["python3", "app.py"]