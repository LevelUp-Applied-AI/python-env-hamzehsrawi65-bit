# Docker Notes — Day 9

## Docker Version

[paste output of: docker version]

## Docker Info

[paste output of: docker info]

## Hello World Test

[paste output of: docker run hello-world]

## Postgres Container

Command used:
```bash
docker run -d --name pg-prework -e POSTGRES_PASSWORD=prework -p 5432:5432 postgres:15-alpine