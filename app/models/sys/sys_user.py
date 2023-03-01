# coding=utf-8
from datetime import datetime
import time
from app.models.base import db
from sqlalchemy import Column, Integer, String, DateTime, Numeric, Boolean, SMALLINT, BigInteger, Float, TEXT, Date
from sqlalchemy.dialects.mysql import LONGTEXT


class SysUser(db.Model):
    '''
    模型(表)备注:
    用户表
    '''
    __tablename__ = 'sys_user'

    '''   创建时间   '''
    create_time = Column(DateTime(), default=datetime.now)

    '''   邮箱   '''
    email = Column(String(64), primary_key=True)

    '''   主键ID   '''
    id = Column(BigInteger(), primary_key=True)

    '''   是否删除（0：未删除，1：删除）   '''
    is_delete = Column(Integer())

    '''   姓名   '''
    name = Column(String(32))

    '''   加盐密码   '''
    password = Column(String(500))

    '''   电话号码   '''
    phone = Column(String(32))

    '''   随机字符串   '''
    stochastic = Column(String(128))

