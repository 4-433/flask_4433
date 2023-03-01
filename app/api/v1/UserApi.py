# -*- coding: utf-8 -*-
"""
@Time ： 2023/3/1 17:33
@Auth ： 冯珂
@File ：UserApi.py
@IDE ：PyCharm
@Motto: 
"""
from app.libs.redprint import Redprint
from app.service.User.UserService import UserService
from app.validators.forms import UserRegisterForm

api = Redprint('user')


@api.route('/register', methods=['POST'])
def register():
    """
    注册用户
    :return:
    """
    form = UserRegisterForm().validate_for_api()
    rm = UserService()
    return rm.register(name=form.name.data, phone=form.phone.data, password=form.password.data, code=form.code.data,
                       logo=form.logo.data, email=form.email.data)
