# Derleme aşaması
# java development kit
FROM openjdk:8-jdk-alpine AS derleyici  
COPY source /usr/src/uygulama
WORKDIR /usr/src/uygulama
RUN javac uygulama.java

# Çalıştırma aşaması
# java runtime environment
FROM openjdk:8-jre-alpine  
WORKDIR /uygulama
COPY --from=derleyici /usr/src/uygulama/ .  
CMD ["java", "uygulama"]

