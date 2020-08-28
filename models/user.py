import sqlite3
from db import db

#User class
#class methos in this class is used for fetcing user details using username or id.
#These functions are also used in authenticate and identity functions in jwt.(security.py)
class UserModel(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))
    
    def __init__(self,username,password):
        self.username = username
        self.password = password

    @classmethod
    def findByUsername(cls, username):
        return cls.query.filter_by(username=username).first()
        
    @classmethod
    def findById(cls, _id):
        return cls.query.filter_by(id=_id).first()
    
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
