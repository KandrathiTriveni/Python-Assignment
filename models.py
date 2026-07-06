from sqlalchemy import Column, Integer, String
from database import Base, engine

class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, autoincrement=True)
    item = Column(String(20), nullable=False)
    status = Column(String(20), nullable=False, default="pending")

Base.metadata.create_all(bind=engine)