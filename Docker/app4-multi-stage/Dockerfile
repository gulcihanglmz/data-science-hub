# Derleme aşaması
FROM openjdk:8-jdk-alpine AS derleyici  # java development kit
COPY source /usr/src/uygulama
WORKDIR /usr/src/uygulama
RUN javac uygulama.java

# Çalıştırma aşaması
FROM openjdk:8-jre-alpine  # java runtime environment
WORKDIR /uygulama
COPY --from=derleyici /usr/src/uygulama/ .  
CMD ["java", "uygulama"]
