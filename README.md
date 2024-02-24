# News

Simple website showing the lastest *n* articles from a selection of news outlets.

Sources are queried on page request. The application has only one user and retrieving the data is quick enough.

## Development

```bash
$ python3 -m venv venv
$ source venv/bin/activate
$ python3 -m pip install -r requirements.txt

$ export FLASK_APP=news
$ export FLASK_ENV=development
$ flask run
```