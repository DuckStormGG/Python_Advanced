FROM python:3.10-slim

RUN mkdir /app

COPY requirements.txt /app/

COPY task2.py /app/

RUN python -m pip install -r /app/requirements.txt

COPY task2.py /app/

WORKDIR /app

ENTRYPOINT ["python", "task2.py"]