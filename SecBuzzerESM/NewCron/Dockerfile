from alpine:latest

RUN set -ex \
    && apk add --update --no-cache python3 py-pip curl rsync jq

CMD cp /image/root /cron/ && chmod 0644 /cron \
  && crond -b -c /cron && touch /var/log/cron.log && tail -F /var/log/cron.log