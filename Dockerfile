FROM python:3.12-slim-bookworm
LABEL org.opencontainers.image.source=https://github.com/vanbalken/news
LABEL org.opencontainers.image.description="News container image"

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 5000

# TODO Fix moet 'gunicorn --bind 0.0.0.0:5000 'news:create_app()'
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "news:create_app()"]
