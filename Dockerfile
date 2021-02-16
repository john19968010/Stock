FROM python:3.9.1-slim
ENV PYTHONUNBUFFERED=1
WORKDIR /stock
COPY . /stock
RUN pip3 install -r requirements.txt
