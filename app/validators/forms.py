from wtforms import StringField, validators, RadioField, IntegerField
from wtforms.validators import DataRequired, Regexp

from app.validators.base import BaseForm


class FileForm(BaseForm):
    is_public_read = IntegerField(validators=[DataRequired(message='必填项')])



