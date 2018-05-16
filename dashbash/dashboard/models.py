import datetime
from dashbash.database import Column, Model, db, Relationship

# Refer: http://docs.sqlalchemy.org/en/latest/orm/basic_relationships.html#many-to-many


class NotesTags(Model):
    __tablename__ = 'notes_tags'
    ntId = Column(db.Integer, primary_key=True, autoincrement=True)
    tagId = Column(db.Integer, db.ForeignKey('tags.tId'), primary_key=True)
    noteId = Column(db.Integer, db.ForeignKey('notes.nId'), primary_key=True)


class Notes(Model):

    __tablename__ = 'notes'
    nId = Column(db.Integer, primary_key=True, autoincrement=True)
    title = Column(db.String(80), nullable=False)
    content = Column(db.Text, nullable=True)
    createDate = Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow)
    tags = Relationship('NotesTags', lazy='joined')


class Tags(Model):

    __tag__ = 'tags'
    tId = Column(db.Integer, primary_key=True, autoincrement=True)
    tag = Column(db.String(30), nullable=False)