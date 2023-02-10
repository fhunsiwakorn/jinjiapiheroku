from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLALCHEMY_DATABASE_URL = "mysql+mysqldb://root:@localhost:3306/jinjidb"
SQLALCHEMY_DATABASE_URL = "mysql://vwlz3iy8y3hto1hm:xvnw1o07t6i32px2@m7az7525jg6ygibs.cbetxkdyhwsb.us-east-1.rds.amazonaws.com:3306/bcl3dk8hy73950vs"
engine = create_engine(SQLALCHEMY_DATABASE_URL,  pool_size=100)



SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    except:
        db.close()
