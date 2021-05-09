FROM python:3.8.3-alpine

WORKDIR /app
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev zlib-dev jpeg-dev

COPY . .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
ENTRYPOINT ["sh", "entrypoint.sh"]