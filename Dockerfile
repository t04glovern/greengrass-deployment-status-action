FROM python:3.9-slim

RUN pip install --no-cache-dir awscli boto3

COPY entrypoint.sh /entrypoint.sh
COPY greengrass_status.py /greengrass_status.py

ENTRYPOINT ["/entrypoint.sh"]
