FROM python:3.9-slim-buster AS builder

ADD . /application/
WORKDIR /application

ENV DJANGO_SETTINGS_MODULE tsimain.settings

COPY requirements.txt /application
RUN pip3 install -r requirements.txt --no-cache-dir

COPY . /application
ENTRYPOINT ["python3"]
CMD ["manage.py", "runserver", "0.0.0.0:8000"]