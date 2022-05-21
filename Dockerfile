FROM python:3.9.10

ENV PORT 1881

WORKDIR /app
COPY . /app

RUN pip install -r requirements.txt

EXPOSE $PORT

CMD python run.py
