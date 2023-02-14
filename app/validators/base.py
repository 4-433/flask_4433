import wtforms_json
from flask import request
from wtforms import Form

from app.libs.error_code import ParameterException


class BaseForm(Form):
    def __init__(self):
        data = request.get_json()
        args = request.args.to_dict()
        super(BaseForm, self).__init__(data=data, **args)

    def validate_for_api(self):
        valid = super(BaseForm, self).validate()
        if not valid:
            raise ParameterException(msg=self.errors)
        return self


class JsonForm(Form):
    """
    作为复杂的json数据做校验
    """

    @classmethod
    def init_and_validate(cls):
        wtforms_json.init()
        form = cls.from_json(request.get_json())
        valid = form.validate()
        if not valid:
            raise ParameterException(msg=form.errors)
        return form
