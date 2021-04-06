from flask import Flask, jsonify
import urllib.request
import datetime
import json
app = Flask(__name__)

# This line to make response Pretty Printed if you want to disable it set it to False
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True


@app.route('/top_repos', methods=['GET'])
def top_repos():
    # fetch starred repos created in last 30 days
    start_date = datetime.datetime.now() - datetime.timedelta(30)
    start_date = start_date.strftime("%Y-%m-%d")
    url = f"https://api.github.com/search/repositories?q=created:>{start_date}&sort=stars&order=desc"

    # Open github url and save it in data var as json
    with urllib.request.urlopen(url) as json_url:
        data = json.loads(json_url.read())

    languages = {}

    for item in data['items']:
        if item['language'] is None:
            item['language'] = "null"

        if item['language'] in languages:
            languages[item['language']]['num_of_repos'] += 1
            languages[item['language']]['repos'].append(item)

        else:
            languages[item['language']] = {'num_of_repos': 1, 'repos': [item]}

    return jsonify(languages)
