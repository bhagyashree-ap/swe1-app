# PollApp

[![Build Status](https://app.travis-ci.com/bhagyashree-ap/swe1-app.svg?branch=main)](https://app.travis-ci.com/bhagyashree-ap/swe1-app)
[![Coverage Status](https://coveralls.io/repos/github/bhagyashree-ap/swe1-app/badge.svg)](https://coveralls.io/github/bhagyashree-ap/swe1-app)

Built PollApp with Django. It lets users view polls, vote and see results. Admin can add and manage polls through the admin page.

## Tech stack

- Python 3.12
- Django 5.2
- SQLite
- AWS Elastic Beanstalk
- Gunicorn and WhiteNoise for serving the app and static files
- Amazon S3 for Elastic Beanstalk deployment bundles
- Travis CI for CI/CD
- Black and Flake8 for formatting and lint checks
- Django tests with coverage.py and Coveralls
