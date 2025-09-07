from .base import *
import dj_database_url
import os # os 모듈 import 추가

# ===============================================================
# 핵심 프로덕션 설정
# ===============================================================
DEBUG = False
IS_TEST = False


# ===============================================================
# 도메인 및 호스트 설정
# ===============================================================
# DOMAIN: 나중에 Heroku 앱 주소로 변경하세요 (예: 'https://your-app-name.herokuapp.com/')
# 이 설정은 이메일 링크 등에서 전체 URL을 생성할 때 사용됩니다.
DOMAIN = 'FIXME'

# ALLOWED_HOSTS: Heroku가 사용하는 도메인을 허용합니다.
# 나중에는 ['your-app-name.herokuapp.com'] 처럼 특정 도메인만 지정하는 것이 더 안전합니다.
ALLOWED_HOSTS = ['*']


# ===============================================================
# 데이터베이스 설정 (Heroku 연동 핵심)
# ===============================================================
# Heroku에서 제공하는 PostgreSQL 데이터베이스를 사용하도록 설정합니다.
# 더 이상 프로젝트의 db.sqlite3 파일을 사용하지 않습니다.
DATABASES = {
    'default': dj_database_url.config(conn_max_age=600, ssl_require=True)
}


# ===============================================================
# 정적 파일 설정 (Heroku 연동 핵심)
# ===============================================================
# Whitenoise가 CSS, JavaScript 같은 정적 파일을 효율적으로 관리하도록 설정합니다.
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'

# Whitenoise 미들웨어를 MIDDLEWARE 목록의 두 번째 위치에 추가합니다.
# 이 설정은 정적 파일 요청을 처리하는 데 중요합니다.
# base.py에서 가져온 MIDDLEWARE 리스트에 whitenoise를 끼워넣는 방식입니다.
if 'MIDDLEWARE' in locals():
    MIDDLEWARE.insert(1, 'whitenoise.middleware.WhiteNoiseMiddleware')


# ===============================================================
# 기타 기존 설정 (유지)
# ===============================================================
RECAPTCHA_SCORE_THRESHOLD = 0.5

GA_CODE = '''
<script>
  /* FIXME */
</script>
'''


# from .base import *

# DEBUG = False

# IS_TEST = False

# # Used for constructing URLs; include the protocol and trailing
# # slash (e.g. 'https://galacticpuzzlehunt.com/')
# DOMAIN = 'FIXME'

# # List of places you're serving from, e.g.
# # ['galacticpuzzlehunt.com', 'gph.example.com']; or just ['*']
# ALLOWED_HOSTS = ['*']

# RECAPTCHA_SCORE_THRESHOLD = 0.5

# # Google Analytics
# GA_CODE = '''
# <script>
#   /* FIXME */
# </script>
# '''
