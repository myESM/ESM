FROM alpine:3

# RUN set -ex \ # for debug
RUN set -e && apk add --update --no-cache python3 py-pip curl \
    && pip install --trusted-host pypi.python.org --trusted-host files.pythonhosted.org --trusted-host pypi.org --upgrade pip \
    && pip install apscheduler --trusted-host pypi.org --trusted-host files.pythonhosted.org
CMD "sleep" "infinity"