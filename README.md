# oz_03_collabo-001-BE

합동 프로젝트 1팀 리포지토리입니다.

# 프론트엔드 로컬 개발을 위해 Docker로 환경 설정 및 실행

### 1. 도커 데스크탑 설치

[도커사이트](https://www.docker.com/)

### 2. 깃클론

```bash
git clone https://github.com/OZ-Coding-School/oz_03_collabo-001-BE.git
```

### 3. 프로젝트 폴더로 이동

```bash
cd oz_03_collabo-001-BE
```

### 4. 독커 컴포즈 실행

```bash
docker-compose -f docker-compose-dev.yml up
```

### 스웨거 페이지 (API 테스트)

```bash
http://127.0.0.1:8000/swagger/
```

### 리독 페이지 (API 문서)

```bash
http://127.0.0.1:8000/redoc/
```

### cicd test 08.23 16:53