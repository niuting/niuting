#!/usr/bin/env python
# encoding: utf-8

import sqlalchemy as sql
import sqlalchemy.ext.declarative as sqle
import sqlalchemy.orm as sqlo

datalist1 = ['name', 'id', 'age']
typelist1 = ['String', 'Integer', 'Integer']
Base = sqle.declarative_base()

URL = 'mysql+mysqldb://root:zhangbo@127.0.0.1:3306/niuting'
engine = sql.create_engine(URL, encoding='utf-8', echo=False)
meta = sql.MetaData('mysql+mysqldb://root:zhangbo@127.0.0.1:3306/niuting')#范围
#Session = sqlo.scoped_session(sqlo.sessionmaker(bind=engine))
#session = Session()

class _UserTable(Base):
    global datalist1
    global typelist1

    __tablename__ = 'us'
    '''
    for (data, types) in zip(datalist1, typelist1):
        if(data.lower() == 'id'):
            data = sql.Column(types,primary_key=True)
        else:
            data = sql.Column(types)
    '''
    id = sql.Column(sql.Integer, primary_key=True)
    name = sql.Column(sql.String)
    age = sql.Column(sql.Integer)
    '''
    def __init__(self, id, name):
        self.id = id
        self.name = name
    '''

Session = sqlo.scoped_session(sqlo.sessionmaker(bind=engine))
session = Session()

user = _UserTable(id = 3, name = 'jia', age = 3)
session.add(user)
session.commit()
