# Hacettepe Free Software Society Website

Our website's backend has been renewed in 2024, because no one wanted to touch Node.js anymore.

You can still access the [legacy repository](https://github.com/hacettepeoyt/website).

## Build

### Configuration

First, you need to have a configuration file written in [toml](https://docs.python.org/3/library/tomllib.html) like the
one below.

```toml
SECRET_KEY = "<your secret key>"
MATRIX_ADMIN_ROOM = "<your matrix room link>"
MATRIX_ACCESS_TOKEN = "<your matrix access token>"
```

If you want to specify, optionally you can add these. If you are building for production, please make sure `DEBUG` is
set to `false`. The values below are the default ones.

```toml
DEBUG = true
ALLOWED_HOSTS = ["*"]
CSRF_TRUSTED_ORIGINS = ["*"]
DATABASE_NAME = "./oytwebsite/db.sqlite3"
STATIC_URL = "static/"
MEDIA_URL = "media/"
MEDIA_ROOT = "./oytwebsite/media"
```

### Virtual Environment

A virtual environment is optional, but highly recommended:

```bash
python3 -m venv venv && source venv/bin/activate
```

### Requirements

You can install required python packages directly from `requirements.txt`.

```bash
pip install -r requirements.txt
```

### Migrations

Create needed database tables first. You don't need to call `makemigrations`, but it's a good idea to run it just in
case. Actually, if you are not going to work with the database, then you can even skip this step, but
**not recommended.**

```bash
python oytwebsite/manage.py makemigrations
python oytwebsite/manage.py migrate
```

### Run

First export your configuration file's path. If you don't export, by default it's assumed to be in `./config.toml`

```bash
export CONFIG_FILE=/path/to/your/config
```

Then run the program with

```bash
python oytwebsite/manage.py runserver
```

or

```bash
PYTHONPATH=oytwebsite django-admin runserver --settings=oytwebsite.settings
```

If you have a different `settings.py`, you can use that instead.

## Contribution

Any type of contribution is appreciated! If you don't want
to [grab an issue](https://github.com/hacettepeoyt/oyt-website), then
please [open a new one](https://github.com/hacettepeoyt/oyt-website/issues/new) first.

## License

[AGPL-3.0](https://github.com/hacettepeoyt/oyt-website/LICENSE)
