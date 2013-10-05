from sqlalchemy import Column, Integer, String

from db import Base, session

class Url(Base):
    """ the table containing the urls, plus additional info """
    
    __tablename__ = "urls"
    
    id = Column(Integer, primary_key=True)
    # id is the number in base 10 which gives the short url in base 62
    long_url = Column(String, unique=True)
    
    def __init__(self, long_url):
        self.long_url = long_url
    
    def store(self):
        session.add(self)
        session.commit()
        
    def __repr__(self):
        return str(self.id) + ": " + self.long_url
    
