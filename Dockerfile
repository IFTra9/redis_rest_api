FROM python:2.7

COPY pyServer.py pyServer.py
COPY redisDB.py redisDB.py
RUN pip install flask
RUN pip install redis
CMD ["python","pyServer.py"]

