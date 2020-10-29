import app as boke

app = boke.configured_app()

# gunicorn appcorn:app
# nohup gunicorn -b '0.0.0.0:80' appcorn:app &

# wsgi
