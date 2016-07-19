
from peewee import *
from playhouse.fields import ManyToManyField
import datetime

from plugins.raw.Model import Raw_Model
from plugins.extract.Model import Extract_Model

db = SqliteDatabase('FoRREST.db')


class Forrest_Model(Model):
    created = DateTimeField(default=datetime.datetime.now)
    sha256sum = CharField(max_length="64")
    raw = ManyToManyField(Raw_Model, related_name='raw')
    extract = ManyToManyField(Extract_Model, related_name='extract')

    class Meta:
        database = db

    @classmethod
    def add_entry(cls, forrest):
        entry = None

        try:
            entry = cls.create(sha256sum=forrest.raw.get_sha256())
            entry.raw.add(forrest.raw.add_entry())
            entry.extract.add(forrest.extract.add_entry())
        except Exception as e:
            print 'Something went wrong with the database'
            print e

        return entry

db.connect()
db.create_tables([
    Forrest_Model,
    Forrest_Model.raw.get_through_model(),
    Forrest_Model.extract.get_through_model(),
], safe=True)
