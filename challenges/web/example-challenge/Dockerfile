FROM php:7.4-apache

# 작업 디렉터리 설정
WORKDIR /var/www/html

# 필요한 패키지 설치
RUN apt-get update && apt-get install -y \
    zip \
    unzip \
    vim \
    && rm -rf /var/lib/apt/lists/*

# PHP 설정
RUN docker-php-ext-install mysqli pdo pdo_mysql

# 소스 코드 복사
COPY src/ /var/www/html/

# 관리자 봇 스크립트 복사 (실제로는 사용하지 않음, 문제 설명용)
COPY admin_bot.js /admin_bot.js

# 권한 설정
RUN chown -R www-data:www-data /var/www/html \
    && chmod -R 755 /var/www/html

# 포트 노출
EXPOSE 80

# 컨테이너 시작 시 실행할 명령어
CMD ["apache2-foreground"] 