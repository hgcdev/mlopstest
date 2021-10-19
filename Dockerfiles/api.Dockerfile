FROM tiangolo/uvicorn-gunicorn:python3.8-slim 

WORKDIR /app 
ENV DEBIAN_FRONTEND=noninteractive
ENV MODULE_NAME=app 
ADD requirements.txt . 
RUN pip install -r requirements.txt \    
    && rm -rf /root/.cache 
COPY ./python .
EXPOSE 5000
CMD ["uvicorn", "--host", "0.0.0.0", "--port", "5000", "app:app"]