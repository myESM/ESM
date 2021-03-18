FROM alpine:latest

RUN set -ex \
    && apk add --update --no-cache python3 py-pip curl vnstat tini \
    && pip install APScheduler \
    && ln -snf /usr/share/zoneinfo/UTC /etc/localtime

ENTRYPOINT ["/sbin/tini", "--"]

CMD "sleep" "infinity"