FROM python:3.6.1-alpine

WORKDIR /coordinate-finder

ADD . /coordinate-finder

RUN pip install -r requirements.txt

CMD ["python","main.py"]