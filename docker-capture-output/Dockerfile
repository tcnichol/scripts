FROM python:3.8

ENV PYTHONUNBUFFERED=0

COPY requirements.txt ./

COPY . /
RUN pip install -r requirements.txt


CMD ["python", "-u" , "main.py"]
