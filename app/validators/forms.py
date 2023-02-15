from wtforms import StringField, validators, RadioField, IntegerField
from wtforms.validators import DataRequired, Regexp

from app.validators.base import BaseForm


class FileGet(BaseForm):
    resource_id = StringField(validators=[DataRequired(message='必填项')])



