FROM python:3.9

WORKDIR /mysqlload

COPY . . 

RUN pip install mysql-connector-python

CMD ["python","mysql-load.py"]
