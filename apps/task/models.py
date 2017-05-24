# -*- coding: utf-8 -*-
# -*- __author__=straw -*-
from sqlalchemy import Column,String,create_engine,Integer,DATETIME,TEXT
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import uuid
import time

# 创建对象的基类:
Base = declarative_base()

class Task(Base):
    ISOTIMEFORMAT='%Y-%m-%d %X'

    __tablename__ = 'task'
    # 表的结构:
    id = Column(String(36), primary_key=True, default=uuid.uuid4().__str__())
    index_ = Column(String(255))
    content = Column(String(3000))
    work_time = Column(String(20))
    question_id = Column(String(100))
    resolution = Column(String(255))
    complete_rate = Column(String(255))
    create_time = Column(DATETIME, default=time.strftime(ISOTIMEFORMAT, time.localtime()))
    user_id = Column(String(36))

