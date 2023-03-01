from datetime import datetime
import json

from sqlalchemy import or_

from Tool.Redis.Redis import Redis
from Tool.communal import Salt
from app.libs.enums import IsDeleteEnum
from app.libs.error_code import AuthFailed, ClientRedoError, Success
from app.models.base import db
from app.models.sys.sys_user import SysUser
from app.service.Base import BaseService


class UserService(BaseService):
    def __init__(self, user={}):
        super().__init__()
        self.user = user

    def register(self, email, name, phone, password, code, logo):
        """
        注册用户
        @param email: 邮箱
        @param name: 用户名
        @param phone: 电话号码
        @param password: 密码
        @param code: 验证码
        @param logo: 头像ID
        @return:
        """
        with db.auto_commit():
            self.user['email'] = email
            self.user['name'] = name
            self.user['phone'] = phone
            # 校验验证码是否正确
            R = Redis()
            verification_str = R.get_str(mobile=phone)
            if verification_str is None:
                raise AuthFailed(msg='验证码已过期！')
            verification_dic = json.loads(verification_str)
            R_code = verification_dic.get('code')
            if R_code != code:
                raise AuthFailed(msg='验证码错误，请重新输入！')

            # 校验邮箱是否重复
            user_query = db.session.query(SysUser.id).\
                filter(or_(SysUser.email == self.user.get('email'), SysUser.phone == self.user.get('phone'))).\
                filter(SysUser.is_delete == IsDeleteEnum.未删除.value).first()
            if user_query:
                raise ClientRedoError(msg="邮箱和手机号已存在，注册失败！")

            # 生成随机字符串
            salt = Salt(random_length=20)
            stochastic = salt.stochastic
            # 密码加密
            encrypted_str = salt.encrypt(password=password)
            # 入库
            user_obj = SysUser()
            user_obj.email = self.user.get('email')
            user_obj.logo = logo
            user_obj.name = self.user.get('name')
            user_obj.phone = self.user.get('phone')
            user_obj.stochastic = stochastic
            user_obj.password = encrypted_str
            user_obj.create_time = datetime.now()
            db.session.add(user_obj)

            return Success(msg='注册成功！')
