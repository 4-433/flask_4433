# -*- coding: utf-8 -*-
"""
@Time ： 2023/2/13 15:39
@Auth ： 冯珂
@File ：__init__.py.py
@IDE ：PyCharm
@Motto: 
"""


def create_app():
    from .app import Flask
    from flask_cors import CORS
    app = Flask(__name__)
    # 解决跨域问题
    CORS(app, resources={r'/*': {'origins': '*'}})
    app.config.from_object('app.config.secure')
    app.config.from_object('app.config.setting')
    register_blueprints(app)
    register_plugin(app)
    return app


def register_blueprints(app):
    from app.api.v1 import create_blueprint_v1
    app.register_blueprint(create_blueprint_v1(), url_prefix='/v1')


def register_plugin(app):
    from app.models.base import db
    # 将db与flask核心对象关联起来
    db.init_app(app)
    with app.app_context():
        db.create_all(app=app)
