FROM python:3.11-slim-bullseye

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PIP_ROOT_USER_ACTION=ignore
ENV PYTHONPATH=/app

COPY . /app

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt
