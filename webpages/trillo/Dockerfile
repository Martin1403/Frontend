FROM python:3.9-slim

# App name
ARG APP="frontend"

RUN mkdir $APP
COPY requirements.txt $APP/requirements.txt
RUN pip install -U pip
RUN pip install -r $APP/requirements.txt
COPY . /$APP

# Settings:
ENV DOCKER=1
ENV QUART_APP=$APP.app:app
ENV QUART_ENV=development
EXPOSE 5003

CMD quart run -h "0.0.0.0" -p 5003