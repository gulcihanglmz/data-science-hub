FROM nginx:latest

LABEL maintainer="Gulcihan gulcihan@gmail.com"
ENV USER="Gulcihan"
ARG COLOR

RUN apt-get update && \
    apt-get install -y curl htop wget

WORKDIR /temporary
ADD https://wordpress.org/latest.tar.gz .

WORKDIR /usr/share/nginx/html
COPY html/${COLOR}/ .

HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 CMD curl -f http://localhost/ || exit 1

CMD ["./script.sh"]
