# 개발 및 호스팅 환경 설정 가이드

이 문서는 보안 동아리 웹사이트를 호스팅하기 위한 환경 설정 방법을 안내합니다.

## 기본 도구 설치

Ubuntu/Debian 기반 시스템에서 필요한 기본 도구를 설치합니다:

```bash
# 시스템 업데이트
sudo apt update
sudo apt upgrade -y

# 기본 도구 설치
sudo apt install -y curl wget git

# Docker 설치
sudo apt install -y docker.io docker-compose

# Docker 사용자 그룹 설정 (sudo 없이 Docker 사용)
sudo usermod -aG docker $USER
newgrp docker

# Python 및 pip 설치
sudo apt install -y python3 python3-pip python3-venv
```

## 방화벽 설정

```bash
# UFW 설치 및 활성화
sudo apt install -y ufw
sudo ufw enable

# 필요한 포트 개방
sudo ufw allow ssh # SSH (22)
sudo ufw allow 80  # HTTP
sudo ufw allow 443 # HTTPS

# 상태 확인
sudo ufw status
```

## 시스템 설정

시스템 리소스를 최적화하기 위한 설정:

```bash
# 스왑 파일 생성 (RAM이 적은 경우)
sudo fallocate -l 4G /swapfile
sudo chmod 600 /swapfile
sudo mkswap /swapfile
sudo swapon /swapfile
echo '/swapfile none swap sw 0 0' | sudo tee -a /etc/fstab

# 시스템 제한 설정
echo "fs.file-max = 65535" | sudo tee -a /etc/sysctl.conf
echo "* soft nofile 65535" | sudo tee -a /etc/security/limits.conf
echo "* hard nofile 65535" | sudo tee -a /etc/security/limits.conf
sudo sysctl -p
```

## Git 저장소 설정

```bash
# 저장소 클론
git clone https://github.com/username/pcode_web.git
cd pcode_web

# 필요한 디렉토리 생성
mkdir -p docker/nginx backend frontend
```

## DDNS 업데이트 클라이언트 설정

```bash
# DDNS 업데이트 스크립트 권한 설정
chmod +x scripts/update_ddns.sh

# DDNS 업데이트 테스트 실행 (DuckDNS 예시)
./scripts/update_ddns.sh duckdns your-domain your-username your-token

# DDNS 자동 업데이트 등록 (15분 간격)
(crontab -l 2>/dev/null; echo "*/15 * * * * $(pwd)/scripts/update_ddns.sh duckdns your-domain your-username your-token > /dev/null 2>&1") | crontab -
```

## Docker 컨테이너 실행

```bash
# Docker 서비스 시작
sudo systemctl start docker
sudo systemctl enable docker

# Docker 컨테이너 실행
docker-compose up -d

# 상태 확인
docker-compose ps
```

## SSL 인증서 설정 (선택사항)

Let's Encrypt를 사용하여 무료 SSL 인증서 발급:

```bash
# Certbot 설치
sudo apt install -y certbot python3-certbot-nginx

# 인증서 발급
sudo certbot --nginx -d your-domain.duckdns.org
```

## 시스템 모니터링 설정 (선택사항)

```bash
# 기본 모니터링 도구 설치
sudo apt install -y htop iotop iftop

# Netdata 모니터링 도구 설치
bash <(curl -Ss https://my-netdata.io/kickstart.sh)
```

## 자동 업데이트 설정 (선택사항)

보안 업데이트 자동화:

```bash
sudo apt install -y unattended-upgrades
sudo dpkg-reconfigure -plow unattended-upgrades
``` 