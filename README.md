## ibx-flask-hypercorn-app

Flask + Hypercorn application for the Fly.io cloud deployment

# Components:
- [Flask](https://github.com/pallets/flask) - Python micro framework
- [Hypercorn](https://github.com/pgjones/hypercorn) - an ASGI and WSGI web server

# Deployment:
0. [Fly.io](https://fly.io) - create account
1. mkdir ibx-flask-hypercorn-app
2. cd ibx-flask-hypercorn-app
3. python -m venv venv
4. .\venv\scripts\activate
5. pip install flask, asgiref, hypercorn
6. create app.py and templates
7. some code
8. pip freeze > requirements.tx
9. flyctl auth login
10. flyctl launch
11. flyctl deploy
12. browse https://ibx-flask-hypercorn-app.fly.dev/
