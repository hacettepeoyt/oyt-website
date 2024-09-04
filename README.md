# Hacettepe Free Software Society Website

Our website's backend has been renewed in 2024, because no one wanted to touch Node.js anymore.

You can still access the [legacy repository](https://github.com/hacettepeoyt/website).

## Development

### Configuration

We handle the configuration by using [toml](https://docs.python.org/3/library/tomllib.html). If not provided, it uses
default values. Optionally, you can set any of the followings in your configuration.

```toml
PORT = "31415"
SECRET_KEY = "unbowed-unbent-unbroken"
MATRIX_ADMIN_ROOM = "<your matrix room link>"
MATRIX_ACCESS_TOKEN = "<your matrix access token>"
DEBUG = true
ALLOWED_HOSTS = ["*"]
CSRF_TRUSTED_ORIGINS = []
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
CONFIG_FILE=/path/to/your/config.toml python oytwebsite/manage.py makemigrations
CONFIG_FILE=/path/to/your/config.toml python oytwebsite/manage.py migrate
```

### Run

```bash
CONFIG_FILE=/path/to/your/config.toml python oytwebsite/manage.py runserver
```

or

```bash
PYTHONPATH=oytwebsite django-admin runserver --settings=oytwebsite.settings
```

If you have a different `settings.py`.

## Contribution

Any type of contribution is appreciated! Consider opening an issue first, if you are planning to add a brand-new future. 

## License

[AGPL-3.0](https://github.com/hacettepeoyt/oyt-website/LICENSE)
