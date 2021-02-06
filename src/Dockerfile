FROM python:3-slim as base
WORKDIR /app
ENV PYTHONUNBUFFERED True
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
