## ibx-flask-hypercorn-app

Flask + Hypercorn application for the Fly.io cloud deployment

# Components
- Flask
- Hypercorn

# Deployment
1. mkdir ibx-flask-hypercorn-app
2. cd ibx-flask-hypercorn-app
3. python -m venv venv
4. .\venv\scripts\activate
5. pip install flask, asgiref, hypercorn
6. create app.py and templates
7. some code
8. flyctl auth login
9. flyctl launch
10. flyctl deploy
11. browse https://ibx-flask-hypercorn-app.fly.dev/