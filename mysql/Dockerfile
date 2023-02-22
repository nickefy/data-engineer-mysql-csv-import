FROM mysql

WORKDIR /mysqlload

COPY . . 

ENV MYSQL_DATABASE mysqltest
ENV MYSQL_ROOT_PASSWORD admin
ADD DDL.sql /docker-entrypoint-initdb.d

EXPOSE 3306