#!/usr/bin/env python3
from flask import Flask, render_template
from flask_babel import Babel
app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """Config class"""
    LANGUAGES = ["en", "fr"]
    app.config['BABEL_DEFAULT_LOCALE'] = 'en'
    app.config['BABEL_DEFAULT_TIMEZONE'] = 'UTC'


app.config.from_object(Config)


@app.route('/')
def hello_world():
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run()
