FROM python:3.7
ADD ./crontask /etc/cron.d/crontask
WORKDIR /srv
RUN pip install -U Flask \
    && apt-get update \
    && apt-get install -y --no-install-recommends cron git wget \
    && apt autoremove -y \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* \
    && chmod 0644 /etc/cron.d/crontask \
    && touch /home/boot.sh \
    && echo "#!/bin/sh\n" > /home/boot.sh \
    && echo "service cron start" >> /home/boot.sh \
    && echo "\n" >> /home/boot.sh \
    && echo "cd /srv/iptv/python && /usr/local/bin/python ./main.py" >> /home/boot.sh \
    && echo "\n" >> /home/boot.sh \
    && echo "/bin/bash" >> /home/boot.sh \
    && mkdir iptv
COPY . /srv/iptv/
WORKDIR /srv/iptv
CMD [ "/bin/bash", "/home/boot.sh" ]
