#!/bin/bash

while ! nc -z "$POSTGRES_HOST" "$POSTGRES_PORT"; do
  sleep 0.1
done

exec python start.py
