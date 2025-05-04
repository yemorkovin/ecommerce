FROM python:3.11

WORKDIR /app

COPY . /app/

COPY requirements.txt .
RUN pip install --upgrade pip && \
    pip install -r requirements.txt
EXPOSE 8000


COPY . .
