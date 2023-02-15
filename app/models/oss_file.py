# coding=utf-8
from datetime import datetime
import time
from app.models.base import db
from sqlalchemy import Column, Integer, String, DateTime, Numeric, Boolean, SMALLINT, BigInteger, Float, TEXT, Date


class OssFile(db.Model):
    """
    模型(表)备注:
    文件信息
    """
    __tablename__ = 'oss_file'

    '''      '''
    id = Column(BigInteger(), primary_key=True)

    '''   私有文件代码   '''
    resource_id = Column(String(64))

    '''   私有文件（key)   '''
    key = Column(String(512), nullable=False)

    '''   文件名   '''
    file_name = Column(String(256))

    '''   文件扩展名   '''
    file_extension = Column(String(32))

    '''   文件大小   '''
    file_size = Column(Integer())

    '''   是否私有（1：私有，0：公有）   '''
    is_private = Column(BigInteger(), nullable=False)

