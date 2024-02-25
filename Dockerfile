FROM python:3.12-slim-bookworm
LABEL org.opencontainers.image.source=https://github.com/vanbalken/news
LABEL org.opencontainers.image.description="News container image"

ENV FLASK_APP=news

WORKDIR /python-docker

RUN pip3 install gunicorn

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["gunicorn", "news:create_app()"]
