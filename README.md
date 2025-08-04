django-docker-example

```bash
sudo apt install python3-venv python3-dev python3-pip
evtl. pip updaten: python.exe -m pip install --upgrade pip

venv namens '.env' erstellen: python -m venv .env

venv aktivieren unter Linux: source .env/bin/activate
oder
venv aktivieren unter Windows: .env\Scripts\activate

in venv (.env) django installieren: pip install django

Projekt anlegen: django-admin startproject demochecklist

Server Testen / Starten: python manage.py runserver
DB initialisieren: python manage.py migrate

Neue App erstellen: python manage.py startapp checklist

```