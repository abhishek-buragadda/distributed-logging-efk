FROM python:3.6-alpine
RUN pip install requests
RUN mkdir /elastic-readiness
ADD isElasticReady.py /elastic-readiness/
RUN chmod 777 /elastic-readiness/isElasticReady.py
CMD ["python","/elastic-readiness/isElasticReady.py"]