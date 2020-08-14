FROM ubuntu:18.04
MAINTAINER CSTI-Chenghan Lin

# Install cron
RUN apt-get update && apt-get install cron curl -y && rm -rf /var/lib/apt/lists/*

# Create the log file to be able to run tail
RUN touch /var/log/cron.log

COPY docker-entrypoint.sh ./

ENTRYPOINT ["/docker-entrypoint.sh"]