from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLALCHEMY_DATABASE_URL = "mysql+mysqldb://root:@localhost:3306/jinjidb"
SQLALCHEMY_DATABASE_URL = "mysql://lsbhpub0pbnz1z7r:fcy5et96ohr2mb5j@m7az7525jg6ygibs.cbetxkdyhwsb.us-east-1.rds.amazonaws.com:3306/yh0oupvbrkee4mi2"
engine = create_engine(SQLALCHEMY_DATABASE_URL,  pool_size=100,
                       max_overflow=15, pool_pre_ping=True, pool_recycle=60*60)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    except:
        db.close()
