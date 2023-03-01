# -*- coding: utf-8 -*-
"""
@Time ： 2023/3/1 17:33
@Auth ： 冯珂
@File ：User.py
@IDE ：PyCharm
@Motto: 
"""
from app.libs.redprint import Redprint
from app.validators.forms import UserRegisterForm

api = Redprint('user')


@api.route('/register', methods=['POST'])
def register():
    """
    注册用户
    :return:
    """
    form = UserRegisterForm().validate_for_api()
    rm = UserService(nickname=form.nickname.data)
    return rm.register(form.phone.data, form.password.data, form.email.data, form.gender.data)