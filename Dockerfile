FROM python:3.4.6-alpine

RUN apk upgrade --update --no-cache

RUN apk add ca-certificates && update-ca-certificates

RUN apk add g++ && apk add make

RUN apk add python-dev

RUN apk add openssl-dev \
    && apk add libxml2-dev \
    && apk add libxslt-dev \
    && apk add libffi-dev

RUN mkdir /app
WORKDIR /app

COPY requirements.txt /app
RUN pip install -r /app/requirements.txt
COPY . /app
ENTRYPOINT ["python"]
CMD ["app.py"]