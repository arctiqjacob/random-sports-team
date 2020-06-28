from flask import Flask, render_template
from random import randrange
import requests
import json
import os

app = Flask(__name__)

NHLAPI = "https://statsapi.web.nhl.com/api/v1/teams/"

@app.route('/')
def index():
    response = requests.get(NHLAPI + str(randrange(1,30))).json()
    team_name = response['teams'][0]['name'].replace(" ", "_").lower()

    return render_template('index.html', response=response, team_name=team_name)

@app.route('/health')
def healthz():
    return json.loads('{ "status":"OK" }')

if __name__ == "__main__":
    app.run(debug=os.environ.get('DEBUG', False),
            host=os.environ.get('HOST', '0.0.0.0'),
            port=os.environ.get('PORT', 8080))