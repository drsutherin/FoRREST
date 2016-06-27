from peewee import *
from playhouse.fields import ManyToManyField
import datetime

db = SqliteDatabase('Idamous.db')


class Raw_Model(Model):
    name = CharField()
    extension = CharField(max_length="32")
    size = BigIntegerField()
    inode = IntegerField()
    path = CharField()
    md5sum = CharField(max_length="32")
    sha1sum = CharField(max_length="40")
    sha256sum = CharField(max_length="64")
    
    created = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db

    @classmethod
    def add_entry(cls, **kwargs):
        try:
            cls.create(
                name = kwargs['name'],
                extension = kwargs['extension'],
                size = kwargs['size'],
                inode = kwargs['inode'],
                path = kwargs['path'],
                md5sum = kwargs['md5sum'],
                sha1sum = kwargs['sha1sum'],
                sha256sum = kwargs['sha256sum']
            )
        except Exception as e:
            print 'Something went wrong with the database'
            print e


db.connect()
db.create_tables([Raw_Model], safe=True)