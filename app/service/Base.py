from flask import request, current_app
from sqlalchemy.orm import Query

from app.libs.error_code import Forbidden


class BaseService:

    def __init__(self):
        self._data = None
        self._files = None
        self._form = None
        self._args = None
        self.user = {}

    def get_data(self, key=None):
        if self._data is None:
            if key:
                self._data = request.get_json(silent=True).get(key)
            else:
                self._data = request.get_json(silent=True)
        return self._data

    def get_files(self, key=None):
        if self._files is None:
            if key:
                self._files = request.files.get(key, None)
            else:
                self._files = request.files
        return self._files

    def get_form(self, key=None):
        if self._form is None:
            if key:
                self._form = request.form.get(key)
            else:
                self._form = request.form
        return self._form

    def get_args(self, key=None):
        if self._args is None:
            if key:
                self._args = request.args.get(key)
            else:
                self._args = request.args
        return self._args

    @staticmethod
    def query_to_dict(data):
        if data is None:
            return {}

        if isinstance(data, Query):
            raise Exception("query_to_dict，数据格式Query")

        if isinstance(data, list):
            raise Exception("query_to_dict，数据格式list")

        result = {}
        if hasattr(data, "__dict__"):  # 实体结果
            for key, value in data.__dict__.items():
                if key != '_sa_instance_state':  # 实体自带属性。不能用del dict[key] 模式,否则实体会移除这个属性，查询报错
                    result[key] = value
        else:  # 匿名结果
            column = data.keys()
            for v in column:
                value = getattr(data, v)
                result[v] = value

        return result

    def query_to_list(self, query):
        if query is None:
            return []
        result = [self.query_to_dict(v) for v in query]
        return result
