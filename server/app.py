# server/app.py
#!/usr/bin/env python3

from flask import Flask, make_response
from flask_migrate import Migrate

from models import db, Earthquake

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)
db.init_app(app)


@app.route('/')
def index():
    body = {'message': 'Flask SQLAlchemy Lab 1'}
    return make_response(body, 200)


@app.route('/earthquakes/<int:id>')
def get_earthquake(id):
    """Return one earthquake as JSON, or a 404 message if the ID doesn't exist."""
    quake = Earthquake.query.filter_by(id=id).first()

    if quake is None:
        return make_response({'message': f'Earthquake {id} not found.'}, 404)

    return make_response(quake.to_dict(), 200)


@app.route('/earthquakes/magnitude/<float:magnitude>')
def get_earthquakes_by_magnitude(magnitude):
    """Return the count and list of earthquakes with magnitude >= the given value.

    An empty result is still a successful query, so it returns 200 with count 0.
    """
    quakes = Earthquake.query.filter(Earthquake.magnitude >= magnitude).all()

    body = {
        'count': len(quakes),
        'quakes': [quake.to_dict() for quake in quakes],
    }
    return make_response(body, 200)


if __name__ == '__main__':
    app.run(port=5555, debug=True)
