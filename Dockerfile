FROM python:3-alpine

RUN mkdir /data
WORKDIR /data

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PORT 8000

RUN apk add --no-cache --update nginx supervisor util-linux wget bash && \
    apk add --no-cache --upgrade musl musl-utils grep && \
    (rm "/tmp/"* 2>/dev/null || true) && (rm -rf /var/cache/apk/* 2>/dev/null || true)

COPY requirements.txt /data
COPY ./data /data
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf
COPY gunicorn.py /opt/gunicorn.py
COPY nginx.conf /etc/nginx/nginx.conf

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

ENTRYPOINT ["/data/entrypoint.sh"]

VOLUME /davegrenier

CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]