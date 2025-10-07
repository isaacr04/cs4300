#!/usr/bin/env bash
set -o errexit

pip install -r homework2/movie_theatre_booking/requirements.txt

python homework2/movie_theatre_booking/manage.py collectstatic --no-input

python homework2/movie_theatre_booking/manage.py migrate