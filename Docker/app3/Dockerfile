# Base image olarak resmi, güncel ve hafif Nginx imajını kullanıyoruz.
FROM nginx:latest

# ====================================================================
# 1. METADATA ve ORTAM AYARLARI
# ====================================================================

# İmajın meta verilerini tanımlıyoruz.
LABEL maintainer=""
LABEL version="1.0"

# Bir ortam değişkeni tanımlıyoruz. Bu varsayılan değeri "run" anında değiştirebiliriz.
ENV KULLANICI="Dunyali"

# ====================================================================
# 2. KURULUM ve DOSYA İŞLEMLERİ
# ====================================================================

# Nginx web kök dizinine geçiyoruz.
WORKDIR /usr/share/nginx/html

# curl aracını kuruyoruz ve hemen temizliyoruz (Dockerfile Best Practice).
# curl, HEALTHCHECK gibi harici kontroller için gereklidir.
RUN apt-get update && \
    apt-get install -y --no-install-recommends curl && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Web sitemizin ana sayfasını Nginx'in sunucu klasörüne kopyalıyoruz.
# Windows dosya sistemi büyük/küçük harf ayırmaz ancak Docker konteksinde
# yazım uyuşmazlığı hata verebilir; mevcut dosya adı `Hello_docker.html`.
COPY Hello_docker.html .

# ====================================================================
# 3. BAŞLANGIÇ KOMUTU (CMD)
# ====================================================================

# CMD komutu, konteyner başlatılırken çalışır ve 3 ana görevi zincirler:
# 1. sed: $KULLANICI metnini, ENV değişkeninin o anki değeriyle değiştirir.
# 2. sed: $HOSTNAME metnini, konteynerin dinamik HOSTNAME değeriyle değiştirir.
# 3. nginx: Nginx'i ana süreç (daemon off) olarak çalıştırır.
CMD sed -e s/Kullanici/"$KULLANICI"/ Hello_docker.html > index1.html && \
sed -e s/Hostname/"$HOSTNAME"/ index1.html > index.html ; \
rm index1.html Hello_docker.html; nginx -g 'daemon off;'