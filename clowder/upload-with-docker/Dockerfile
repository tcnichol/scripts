FROM python:3.8

ENV APIKEY=bcf0504f-7d3f-43c9-90eb-abd7254eebfb

ENV PYTHONUNBUFFERED=0

COPY . /

RUN pip install pyclowder

CMD ["python", "-u", "upload.py"]