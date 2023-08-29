# docker build -t selenium_service .
FROM --platform=linux/amd64 python:3.11-slim

ENV PYTHONIOENCODING utf-8
ENV TZ="Asia/Tokyo"
ENV LANG=C.UTF-8
ENV LANGUAGE=en_US:en

WORKDIR /app

# Install dependencies
COPY ./requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir --upgrade -r /tmp/requirements.txt

COPY ./app/ /var/www/app/

WORKDIR /var/www

EXPOSE 8080
CMD ["uvicorn", "app.main:app", "--reload", "--host", "0.0.0.0", "--port", "8080"]
