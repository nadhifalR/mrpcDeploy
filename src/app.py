from flask import Flask, render_template, request, redirect, jsonify
from datetime import datetime
from pcpartpicker import API
import pandas as pd
import json
from .config import app_config
from .models import db, bcrypt
from .views.UserView import user_api as user_blueprint
from .views.BuildView import build_api as build_blueprint
from .views.PartsView import parts_api as parts_blueprint
from flask_cors import CORS

def create_app(env_name):
    """
    Create app
    """
    
    # app initiliazation
    app = Flask(__name__)

    app.config.from_object(app_config[env_name])

    cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

    # initializing bcrypt
    bcrypt.init_app(app) # add this line
    db.init_app(app) # add this line

    app.register_blueprint(user_blueprint, url_prefix='/api/v1/users')
    app.register_blueprint(build_blueprint, url_prefix='/api/v1/builds')
    app.register_blueprint(parts_blueprint, url_prefix='/api/v1/parts')
    
    """
    api=API()
    parts_data=api.retrieve_all()
    data=parts_data.to_json()
    hmm=json.loads(data)
    """

    @app.route('/')
    def index():
        return render_template('index.html')

    #@app.route('/simulation', methods=['GET'])
    #def simulation():
    #    return jsonify({'status': 'success', 'parts': hmm})

    return app


