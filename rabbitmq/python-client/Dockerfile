FROM python:3-alpine

WORKDIR /work

RUN pip install --upgrade pip && pip install flask pika json-logging

COPY app.py ./ 

CMD ["flask", "run", "--host=0.0.0.0"]
