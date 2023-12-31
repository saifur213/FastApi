from sqlalchemy import Column, Integer, String
from database import Base

# Create Model
class Blog(Base):
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    body = Column(String)