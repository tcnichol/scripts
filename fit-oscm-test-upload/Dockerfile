FROM python:3.9.10-slim-buster AS builder

RUN python -m pip install --upgrade pip

#Install Cron
RUN apt-get update
RUN apt-get -y install cron
RUN apt-get -y install vim

COPY test.py ./home/test.py

COPY run.sh ./home/run.sh

RUN  chmod +x /home/run.sh

# Add crontab file in the cron directory
ADD test-cron /etc/cron.d/test-cron

# Give execution rights on the cron job
RUN chmod 0644 /etc/cron.d/test-cron

# Create the log file to be able to run tail
RUN touch /var/log/cron.log

# Run the command on container startup
CMD cron && tail -f /var/log/cron.log

