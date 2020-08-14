#!/bin/sh

# Add shell script and grant execution rights
chmod +x /script/*.sh

# Give execution rights on the cron job
chmod 0644 /etc/cron.d/simple-cron
chgrp root /etc/cron.d/simple-cron
chown root /etc/cron.d/simple-cron

# Run the command on container startup
cron && tail -f /var/log/cron.log