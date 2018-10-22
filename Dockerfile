FROM python:3.6

ADD ./requirements.txt /
RUN pip install -r /requirements.txt

ADD ./src/ /src
ADD ./templates /templates

ENV FLASK_APP=/src/app.py
CMD flask run --host=0.0.0.0 --port=8000