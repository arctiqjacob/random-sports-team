from flask import Flask, render_template
import random
import requests
import json
import os

app = Flask(__name__)

SPORTSAPI = 'https://www.thesportsdb.com/api/v1/json/1/search_all_teams.php?l='
SPORT=os.environ.get('SPORT', 'NHL')

@app.route('/')
def index():
    response = requests.get(SPORTSAPI+SPORT).json()
    random_team = random.choice(response['teams'])
    return render_template('index.html', random_team=random_team)

@app.route('/health')
def healthz():
    return json.loads('{ "status":"OK" }')

if __name__ == "__main__":
    app.run(debug=os.environ.get('DEBUG', False),
            host=os.environ.get('HOST', '0.0.0.0'),
            port=os.environ.get('PORT', 8080))