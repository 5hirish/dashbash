# -*- coding: utf-8 -*-
"""Database module, including the SQLAlchemy database object and DB-related utilities."""
from dashbash.extensions import db

# Alias common SQLAlchemy names
Column = db.Column
Relationship = db.relationship
Model = db.Model
Session = db.session