
# 1단계: 빌드 환경 설정
# fly.toml에서 사용하던 빌드팩 이미지를 기반으로 시작합니다.
FROM paketobuildpacks/builder:base AS builder

# 작업 디렉터리 설정
WORKDIR /workspace

# 모든 소스 코드를 이미지 안으로 복사
COPY . .

# 빌드팩을 실행하여 앱을 빌드합니다. (Python, pip install 등 자동 수행)
RUN /cnb/lifecycle/builder \
  -app /workspace \
  -layers /layers \
  -group /layers/group.toml \
  -plan /layers/plan.toml

# 2단계: 최종 실행 환경 설정
# 실제 앱이 실행될 더 가볍고 안전한 이미지에서 시작합니다.
FROM paketobuildpacks/run:base-cnb

# --- 사용자 정의 시작 ---
# 패키지 설치를 위해 root 권한으로 잠시 변경
USER root
# wget과 curl을 설치하고, 불필요한 캐시는 삭제하여 이미지 크기를 줄입니다.
RUN apt-get update && apt-get install -y wget curl && rm -rf /var/lib/apt/lists/*
# 보안을 위해 다시 기본 사용자인 cnb로 전환
USER cnb
# --- 사용자 정의 종료 ---

# 1단계에서 빌드팩이 만든 애플리케이션 레이어를 복사
COPY --from=builder /layers /layers

# 앱 실행 명령어 설정 (fly.toml의 processes.app과 동일하게)
CMD ["gunicorn", "-c", "gph/gunicorn.py", "--log-file", "-", "gph.wsgi"]

