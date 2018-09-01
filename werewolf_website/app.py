from flask import Flask, render_template

from .assets import assets
from .blueprints.season import bp as season_blueprint

app = Flask(__name__)
assets.init_app(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/contact/')
def contact():
    return render_template('contact.html')


app.register_blueprint(season_blueprint, url_prefix='/season')

if __name__ == '__main__':
    app.run()
