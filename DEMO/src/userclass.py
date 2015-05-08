#!/usr/bin/env python
# encoding: utf-8

import sqlalchemy as sql
import sqlalchemy.ext.declarative as sqle
import sqlalchemy.orm as sqlo


class UserSql(object):
    '''The basic configuration to the database'''

    def __init__(self):
        '''The basic configuration to initialize the database'''

        URL = 'mysql+mysqldb://root:zhangbo@127.0.0.1:3306/niuting'
        self.engine = sql.create_engine(URL, encoding='utf-8', echo=False)
        self.meta = sql.MetaData('mysql+mysqldb://root:zhangbo@127.0.0.1:3306/niuting')#范围
        self.Session = sqlo.scoped_session(sqlo.sessionmaker(bind=self.engine))

    def get_engine(self):
        '''Get the value of the engine'''

        return self.engine

    def get_mate(self):
        '''Get the value of the mate'''
        meta = sql.MetaData('mysql+mysqldb://root:zhangbo@127.0.0.1:3306/niuting')
        return meta

    def get_session(self):
        '''Get the session class'''

        Session = sqlo.scoped_session(sqlo.sessionmaker(bind=self.engine))
        session = Session()
        return session


    Base = sqle.declarative_base()
    class _UserTable(Base):
        '''Create user table'''

        __tablename__ = 'user_info'
        name = sql.Column(sql.String(20), nullable=False)
        id = sql.Column(sql.Integer, primary_key=True)
        age = sql.Column(sql.Integer, nullable=False)

        def __init__(self, id, name, age):
            '''Create table'''

            self.name = name
            self.id = id
            self.age = age

        def get_table_name(self):
            #   The name of the data table is returned to the user

            return  self.__tablename__

if __name__ == '__main__':
    db = UserSql()
    session = db.get_session()
    user = UserSql._UserTable('niuting', 120, 5)
    session.add(user)
    session.commit()
