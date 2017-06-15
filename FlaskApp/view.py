from FlaskApp import app
from FlaskApp.model import Person
from FlaskApp.config import Config
from flask import render_template, Response, request
import json
from werkzeug.exceptions import BadRequest


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/persons/list')
def get_persons():
    return Response(json.dumps(Person(Config()).read_all()), mimetype='application/json')


@app.route('/persons/delete')
def remove_person():
    id_ = request.args.get('id')
    Person(Config()).remove(id_)
    return 'Removed successfully'


@app.route('/persons/add', methods=['post'])
def add_person():
    name = request.form.get('name')
    comment = request.form.get('comment')
    if not name:
        raise BadRequest('Person was not added. Name can not be empty')
    Person(Config()).add(name, comment)
    return 'Added successfully'


@app.route('/get_winners')
def get_winners():
    return Response(json.dumps(Person(Config()).read_random(3)), mimetype='application/json')
