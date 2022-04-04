FROM python:3.7.6

WORKDIR /coordinate-finder

ADD . /coordinate-finder

RUN pip install numpy
COPY requirements.txt ./requirements.txt
RUN pip install -r requirements.txt


CMD ["python","main.py"]
