FROM fluent/fluentd:v1.9-1
MAINTAINER CSTI-Chenghan Lin

USER root

RUN apk add --no-cache --update --virtual .build-deps \
        sudo build-base ruby-dev \
 # cutomize following instruction as you wish
 && sudo gem install elasticsearch -v 7.6.0 \
 && sudo gem install fluent-plugin-elasticsearch \
                     fluent-plugin-rewrite-tag-filter \
                     fluent-plugin-newsyslog \
                     fluent-plugin-grok-parser \
                     fluent-plugin-parser_cef \
                     fluent-plugin-kvp-filter \
 && sudo gem sources --clear-all \
 && apk del .build-deps \
 && rm -rf /home/fluent/.gem/ruby/2.5.0/cache/*.gem

COPY entrypoint.sh /bin/
USER root
