#!/usr/bin/env python3
import multiprocessing

# workers = multiprocessing.cpu_count() * 2 + 1
workers = 2

bind = '0.0.0.0:8000'

# 아래 라인을 'sync'로 변경합니다.
# 기존: worker_class = 'uvicorn.workers.UvicornWorker'
worker_class = 'sync'

loglevel = 'error'
pidfile = 'gunicorn.pid'

# 프로덕션 환경에서는 이 옵션을 비활성화하는 것이 좋습니다.
# reload = True
