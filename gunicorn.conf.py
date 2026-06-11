# gunicorn.conf.py - إعدادات Gunicorn لـ Render
import os
import multiprocessing

# ==== Bind ====
# Render يستخدم PORT من متغير البيئة
bind = f"0.0.0.0:{os.environ.get('PORT', '5000')}"

# ==== Workers ====
# في Render Free: worker واحد فقط (الذاكرة محدودة)
workers = int(os.environ.get("GUNICORN_WORKERS", "1"))
threads = int(os.environ.get("GUNICORN_THREADS", "4"))
worker_class = "gthread"

# ==== Timeouts ====
# OCR ومعالجة PDF قد تستغرق وقتاً
timeout = int(os.environ.get("GUNICORN_TIMEOUT", "120"))
graceful_timeout = 30
keepalive = 5

# ==== Limits ====
max_requests = 1000
max_requests_jitter = 100
limit_request_line = 8190

# ==== Logging ====
# في Render: استخدام stdout/stderr
accesslog = "-"
errorlog = "-"
loglevel = os.environ.get("GUNICORN_LOG_LEVEL", "info")

# ==== Process naming ====
proc_name = "musaid"

# ==== Security ====
forwarded_allow_ips = "*"