FROM python:alpine
WORKDIR /usr/src/app
ENV PYTHONUNBUFFERED=1
COPY . .
RUN pip3 install -r requirements.txt