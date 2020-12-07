FROM alpine:3

RUN set -ex \
    && apk add --update --no-cache python3 py-pip curl \
    && pip install APScheduler

CMD "sleep" "infinity"