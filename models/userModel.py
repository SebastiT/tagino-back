from sqlalchemy import Column, Integer, String,DateTime, Boolean, Date
from datetime import datetime
from config.db import Base

class User(Base):
  __tablename__ = "users"
  
  id = Column(Integer, primary_key=True, index=True)
  name = Column(String(100), nullable=False)
  
  

class Document(Base):
  __tablename__ = "documents"
  id = Column(Integer, primary_key=True,index=True)
  date = Column(String(255), nullable=False)
  url = Column(String(255), nullable=False)
  type = Column(String(50), nullable=False)
  grade = Column(Integer, nullable=False)
  section = Column(String(1), nullable=False)
  report = Column(Boolean, default=False)
  upload_date = Column(DateTime,default=datetime.utcnow)

  
