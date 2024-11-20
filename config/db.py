from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "mysql+pymysql://root:Abcdario18989$$@localhost:3306/taginoproject"

# DATABASE_URL = "mysql+pymysql://root:lvcqnfZsAWKHIsqOnyxKOtjFxozsxPal@autorack.proxy.rlwy.net:20955/railway"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

meta = MetaData()
meta.reflect(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# conn = engine.connect()