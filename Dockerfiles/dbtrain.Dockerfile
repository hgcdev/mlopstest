FROM mysql:latest
ENV MYSQL_ROOT_PASSWORD=example
ENV MYSQL_DATABASE=data
ENV MYSQL_USER=user
ENV MYSQL_PASSWORD=user123
COPY /data/Iris.csv /tmp/
EXPOSE 3306
COPY ./sql-scripts/ /docker-entrypoint-initdb.d/