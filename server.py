from flask import Flask, jsonify
import urllib.request
import datetime
import json
app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

@app.route('/top_repos', methods=['GET'])
def top_repos():
    start_date = datetime.datetime.now() - datetime.timedelta(30)
    start_date = start_date.strftime("%Y-%m-%d")
    url = f"https://api.github.com/search/repositories?q=created:>{start_date}&sort=stars&order=desc"

    with urllib.request.urlopen(url) as json_url:
        data = json.loads(json_url.read())

    languages = {}

    for item in data['items']:
        if item['language'] is None:
            item['language'] = "None"

        if item['language'] in languages:
            languages[item['language']]['num_of_repos'] +=1
            languages[item['language']]['repos'].append(item)

        else:
            languages[item['language']] = {'num_of_repos': 1, 'repos': [item]}

    return jsonify(languages)
