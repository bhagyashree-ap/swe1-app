# PollApp

[![Build Status](https://travis-ci.com/bhagyashree-ap/swe1-app.svg?branch=main)](https://travis-ci.com/bhagyashree-ap/swe1-app)
[![Coverage Status](https://coveralls.io/repos/github/bhagyashree-ap/swe1-app/badge.svg?branch=main)](https://coveralls.io/github/bhagyashree-ap/swe1-app?branch=main)

Built PollApp with Django. It lets users view polls, vote and see results. Admin can add and manage polls through the admin page.

## Tech stack

- Python 3.12
- Django 5.2 LTS
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

Travis CI runs Black, Flake8, and the Django test suite on pushes and pull requests. Successful builds on `main` deploy to Elastic Beanstalk. Enable the `bhagyashree-ap/swe1-app` repository in Travis CI and Coveralls, then configure these Travis environment variables for deployment:

- `AWS_ACCESS_KEY_ID`
- `AWS_SECRET_ACCESS_KEY`
- `COVERALLS_REPO_TOKEN` (from Coveralls)

The Elastic Beanstalk region, application, environment, and S3 bucket are configured in `.travis.yml`.

After the first Travis build, protect the `main` branch in GitHub and require the Travis CI status check to pass before merging.
