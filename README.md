## ibx-flask-hypercorn-app

Flask + Hypercorn application for the Fly.io cloud deployment

# Components:
- [Flask](https://github.com/pallets/flask): The Python micro framework for building web applications.
- [Hypercorn](https://github.com/pgjones/hypercorn): Hypercorn is an ASGI and WSGI Server.
- [Fly.io](https://fly.io): Fly is a platform for running full stack apps and databases.

# Deployment:
0. [Fly.io](https://fly.io) - create account
1. mkdir ibx-flask-hypercorn-app
2. cd ibx-flask-hypercorn-app
3. python -m venv venv
4. .\venv\scripts\activate
5. pip install flask, asgiref, hypercorn
6. pip freeze > requirement.txt
7. create app.py and templates
8. some code
9. flyctl auth login
10. flyctl launch
11. configure Procfile
12. flyctl deploy
13. browse https://ibx-flask-hypercorn-app.fly.dev/