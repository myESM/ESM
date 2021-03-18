FROM alpine:3

RUN set -ex \
    && apk add --update --no-cache python3 py-pip curl tini \
    && pip install APScheduler


ENTRYPOINT ["/sbin/tini", "--"]

CMD "sleep" "infinity"