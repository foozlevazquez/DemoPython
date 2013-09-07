
from sqlalchemy import Column, Integer, Index, Text, DateTime, String, Text
from sqlalchemy import Table, create_engine, MetaData
import pdb

class MyDB():

    @classmethod
    def init(cls, url, echo=True, **kwargs):
        cls.engine = create_engine(url, echo=echo, **kwargs)
        cls.metadata = MetaData()
        cls.metadata.bind = cls.engine


    @classmethod
    def create_tables(cls):
        cls.t1 = Table('t1', cls.metadata,
                   Column('seqid', Integer, primary_key=True,
                          autoincrement=True),
                   Column('serverid', String(50)),
                   Column('data', Text),
                   )
        cls.t2 = Table('t2', cls.metadata,
                   Column('seqid', Integer, primary_key=True,
                          autoincrement=True),
                   Column('serverid', String(50)),
                   Column('data', Text),
               )

        cls.metadata.create_all()

    @classmethod
    def do_inserts(cls):
        count = 0
        for table in (cls.t1, cls.t2,):
            for i in range(10):
                data = "Data-{}".format(count)
                count += 1
                table.insert(serverid='foo', data=data)).execute()

    @classmethod
    def do_join(cls):
        return cls.t1.join(cls.t2, (cls.t1.c.serverid == cls.t2.c.serverid))

    @staticmethod
    def main(url='sqlite:///:memory:'):
        MyDB.init(url)
        MyDB.create_tables()

        MyDB.do_inserts()
        pdb.set_trace()
        print(MyDB.do_join())
