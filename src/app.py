from collections import defaultdict

from flask import Flask
from flask import render_template
from flask import request

from .main import Parser


app = Flask(__name__, template_folder='../templates')


@app.route('/')
def index():
    p = Parser()

    search_word = request.args.get('search')

    results_raw = p.results()
    if search_word:  # simple search for appropriate games
        results = defaultdict(list)
        for category, games in results_raw.items():
            for game in games:
                if search_word in game:
                    results[category].append(game)
    else:
        results = results_raw

    return render_template("index.html", results=results)
