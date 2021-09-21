#!/usr/bin/python3
"""index file"""

from api.v1.views import app_views
from flask import jsonify
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models import storage


@app_views.route('/status', strict_slashes=False)
def status():
    """ Status of API """
    return jsonify({"status": "OK"})


@app_views.route('/stats', strict_slashes=False)
def count_method():
    """method that return the count
    from each clasess"""

    classes = {"Amenity": Amenity, "BaseModel": BaseModel, "City": City, "Place\
        ": Place, "Review": Review, "State": State, "User": User}

    count_clases = {}
    for key, value in classes.items():
        count_clases[key] = storage.count(value)
    return jsonify(count_clases)
