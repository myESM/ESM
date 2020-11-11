FROM alpine:3

# RUN set -ex \ # for debug
RUN set -e && apk add --update --no-cache python3 py-pip curl \
    && pip install --upgrade pip \
    && pip install apscheduler
CMD "sleep" "infinity"