from flask import Flask
app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/top_repos', methods=['GET'])
def top_repos():
    return 'it works'
