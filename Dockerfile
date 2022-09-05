FROM python:3.10.2

WORKDIR /usr/src/traineeship

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY ./requirements.txt /usr/src/requirements.txt
RUN pip install -r /usr/src/requirements.txt

COPY . /usr/src/traineeship/

EXPOSE 8000
CMD ("python", "manage.py", "runserver", "0.0.0.0:8000")