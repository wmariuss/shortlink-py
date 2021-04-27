FROM python:3.6
LABEL description="ShortLink"
LABEL maintainer="me@marius.xyz"

ENV LC_ALL C.UTF-8
ENV LANG C.UTF-8
ENV PYTHONUNBUFFERED 1

COPY . /opt

WORKDIR  /opt

RUN pip install pipenv
RUN pipenv install --deploy --system

EXPOSE 5000

CMD ["flask", "run"]
