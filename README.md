Anomalous `AdminMiddleware` serialization behavior reproducer
=============================================================

Tested on Python 3.8.

Prerequisites:

- Redis running on locallhost:6379

Steps:

- create and activate a new virtualenv
- `pip install -r requirements.txt`
- `./manage.py migrate`
- `./manage.py runserver`
- `./manage.py rundramatiq --processes 1 --threads 1`
- `curl http://localhost:8000/repro/`
