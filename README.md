# PollApp

## What the app does

Built PollApp with Django. It lets users view polls, vote and see results. Admin can add and manage polls through the admin page.

## Tech stack

- Python 3.12
- Django 6.1
- SQLite
- AWS Elastic Beanstalk
- Gunicorn and WhiteNoise

## Run locally

From the project folder, run:

```bash
python3 -m venv venv
source venv/bin/activate
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Open <http://127.0.0.1:8000/polls/> to view polls.

Open <http://127.0.0.1:8000/admin/> to add questions and choices.

## Deployment

PollApp is deployed on AWS Elastic Beanstalk. The deployed app uses a separate database from the local app.
