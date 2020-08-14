FROM ubuntu:18.04
MAINTAINER CSTI-Chenghan Lin

# Install cron & Python
RUN apt-get update \
  && apt-get install -y cron curl rsync
 
COPY requirement.txt /requirement.txt

RUN set -ex \
    && apt-get install -y python3-pip python3-dev \
    && cd /usr/local/bin \
    && ln -s /usr/bin/python3 python \
    && pip3 install --upgrade pip \
    && rm -rf /var/lib/apt/lists/* \
    && pip3 install -r /requirement.txt

# Copy cronjobs file to the cron.d directory
COPY cronjobs /etc/cron.d/cronjobs

# Give execution rights on the cron job
RUN chmod 0644 /etc/cron.d/cronjobs

# Apply cron job
RUN crontab /etc/cron.d/cronjobs

# Create the log file to be able to run tail
RUN touch /var/log/cron.log

# Setup single cron job
# RUN (crontab -l ; echo "@daily python /script/diskcheck.py >> /var/log/cron.log") | crontab

# Run the command on container startup

CMD echo "Starting" && echo "Continuing" && (cron) \
 && echo "Tailing..." && : >> /var/log/cron.log && tail -f /var/log/cron.log