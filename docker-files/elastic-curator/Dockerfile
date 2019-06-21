FROM python:3.6-alpine

RUN pip install  elasticsearch-curator==5.5.4 &&\
    rm -rf /var/cache/apk/*
RUN pip install 'PyYAML==3.13' --force-reinstall
