from flask import Flask
from flask import Flask
import urllib.request
import datetime
import json
app = Flask(__name__)

@app.route('/top_repos', methods=['GET'])
def top_repos():
    start_date = datetime.datetime.now() - datetime.timedelta(30)
    start_date = start_date.strftime("%Y-%m-%d")
    url = f"https://api.github.com/search/repositories?q=created:>{start_date}&sort=stars&order=desc"

    with urllib.request.urlopen(url) as json_url:
        data = json.loads(json_url.read())

    
    return 'it works'
