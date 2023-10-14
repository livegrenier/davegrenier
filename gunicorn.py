bind = '0.0.0.0:8000'
workers = 1
timeout = 960000
loglevel = 'debug'
accesslog = '/var/log/gunicorn_access_log_app'
errorlog =  '/var/log/gunicorn_error_log_app'
