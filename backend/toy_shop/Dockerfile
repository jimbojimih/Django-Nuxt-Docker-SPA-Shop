FROM python:3.10-buster
ENV PYTHONDONTWRITEBYTECODE=1 
ENV PYTHONUNBUFFERED=1 
WORKDIR /usr/src/backend
COPY requirements.txt /usr/src/backend
RUN pip install -r requirements.txt
EXPOSE 8000