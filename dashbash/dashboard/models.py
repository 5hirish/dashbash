import datetime
from dashbash.database import Column, Model, db, reference_col, Relationship


notesTags = db.Table('notesTags',
                     db.Column('tId', db.Integer, db.ForeignKey('Tags.tId'), primary_key=True),
                     db.Column('nId', db.Integer, db.ForeignKey('Notes.nId'), primary_key=True)
                     )


class Notes(Model):

    __tablename__ = 'notes'
    nId = Column(db.Integer, primary_key=True)
    title = Column(db.String(80), nullable=False)
    content = Column(db.Text, nullable=True)
    createDate = Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow)
    tags = Relationship('Tag', secondary=notesTags, lazy='joined', backref=db.backref('notes', lazy=True))


class Tags(Model):

    __tag__ = 'tags'
    tId = Column(db.Integer, primary_key=True)
    tag = Column(db.String(30), nullable=False)