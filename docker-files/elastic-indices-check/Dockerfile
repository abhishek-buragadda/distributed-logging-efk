FROM python:3.6-alpine
RUN pip install requests
RUN mkdir /elastic-indices
ADD checkIndices.py /elastic-indices/
RUN chmod 777 /elastic-indices/checkIndices.py
CMD ["python","/elastic-indices/checkIndices.py"]