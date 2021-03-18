FROM alpine:3

# RUN set -ex \ # for debug
RUN set -e && apk add --update --no-cache python3 py-pip curl tini \
    && pip install --upgrade pip \
    && pip install apscheduler

ENTRYPOINT ["/sbin/tini", "--"]

CMD "sleep" "infinity"