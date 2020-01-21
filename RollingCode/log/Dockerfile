FROM jfloff/alpine-python:2.7

WORKDIR /app

ADD requirements.txt /app/

RUN pip install --trusted-host pypi.python.org -r requirements.txt

ADD . /app

CMD ["bash", "prestart.sh"]
