#encoding=utf-8
#author:straw
#初始化数据库连接
from sqlalchemy import Column,String,create_engine,Integer,DATETIME
from sqlalchemy.orm import sessionmaker

engine = create_engine('mysql+mysqlconnector://root:1234@127.0.0.1:3306/test', echo=True)
#创建DBSession类型
Session = sessionmaker(bind=engine, expire_on_commit=False)
