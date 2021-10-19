FROM  python:3.9.6
USER root

RUN apt-get update
RUN apt-get install libsasl2-dev
RUN apt-get install -y gnupg2 
RUN apt-get install -y unixodbc-dev
RUN apt-get install -y sasl2-bin libsasl2-2 libsasl2-dev libsasl2-modules libsasl2-modules-gssapi-mit

RUN pip install sasl
RUN pip install thrift
RUN pip install thrift_sasl
RUN pip install PyHive
RUN pip install pandas
RUN pip install pyodbc
RUN pip install datetime
RUN pip install mysql-connector-python
RUN pip install mlflow
RUN pip install scikit-learn
RUN pip install joblib
