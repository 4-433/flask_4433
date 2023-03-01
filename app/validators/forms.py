from wtforms import StringField, validators, RadioField, IntegerField
from wtforms.validators import DataRequired, Regexp

from app.validators.base import BaseForm


class FileGet(BaseForm):
    resource_id = StringField(validators=[DataRequired(message='必填项')])


class UserRegisterForm(BaseForm):
    name = StringField(validators=[DataRequired(message='登录名不允许为空'),
                                   validators.Length(max=8, min=3, message="用户名长度必须大于%(min)d且小于%(max)d")])
    password = StringField(validators=[DataRequired(message='密码不允许为空'), Regexp(
        regex=r'^(?=.*[0-9])(?=.*[A-Z])(?=.*[a-z])(?=.*[!@#$%^&*,\._])[0-9a-zA-Z!@#$%^&*,\\._]{8,12}$',
        message="密码必须包含大小写字母,特殊字符和数字，且长度不低于8位")])
    email = StringField(validators=[DataRequired(message='邮箱不允许为空'), Regexp(
        regex=r'^([a-zA-Z0-9_-])+@([a-zA-Z0-9_-])+(.[a-zA-Z0-9_-])+',
        message="请输入正确的邮箱格式")])
    phone = StringField(validators=[DataRequired(message='电话不允许为空'), Regexp(regex=r'^1\d{10}$', message="输入正确的电话号码！")])
    code = StringField()

