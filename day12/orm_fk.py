# @Time    : 2018/7/23 17:25
# @Author  : Jennings
# @Email   : zjn@wiwi.ink

from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy import func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("mysql+pymysql://Jennings:um7cpphy@106.14.3.173/wiwi?charset=utf8", encoding='utf-8')
# echo=True 打印详细信息

Base = declarative_base()  # 生成orm基类


class User(Base):
    __tablename__ = 'user'  # 表名
    id = Column(Integer, primary_key=True)
    name = Column(String(32))
    password = Column(String(64))

    def __repr__(self):
        return "<%s name:%s password:%s>" % (self.id, self.name, self.password)

