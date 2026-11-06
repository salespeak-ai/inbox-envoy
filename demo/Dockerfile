FROM python:3.13-alpine
WORKDIR /work
COPY adapter/questioner.py /work/adapter/questioner.py
COPY demo/seller.py /work/demo/seller.py
COPY demo/config.json /work/demo/config.json
COPY demo/input.json /work/demo/input.json
RUN adduser -D -u 10001 envoy
USER envoy
