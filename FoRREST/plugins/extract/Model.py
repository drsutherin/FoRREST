from peewee import *
import datetime

from playhouse.fields import ManyToManyField

db = SqliteDatabase('FoRREST.db')


class Section_Model(Model):
    section = CharField()

    class Meta:
        database = db

    @classmethod
    def add_entry(cls, section):
        entry = None

        try:
            entry = cls.create(
                section=section
            )
        except Exception as e:
            print 'Something went wrong with the database'
            print e

        return entry


class Extract_Model(Model):
    filetype = CharField()
    version = CharField()
    architecture = CharField()
    compiler = CharField()
    sections = ManyToManyField(Section_Model, related_name='sections')
    
    created = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db

    @classmethod
    def add_entry(cls, **kwargs):
        entry = None

        try:
            entry = cls.create(
                filetype = kwargs['filetype'],
                version = kwargs['version'],
                architecture = kwargs['architecture'],
                compiler = kwargs['compiler'],
            )
            for item in kwargs['sections']:
                entry.sections.add(Section_Model.add_entry(item))
        except Exception as e:
            print 'Something went wrong with the database'
            print e

        return entry

db.connect()
db.create_tables([Extract_Model, Section_Model, Extract_Model.sections.get_through_model()], safe=True)
