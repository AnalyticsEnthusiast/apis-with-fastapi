
#import psycopg2
import configparser
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

config = configparser.ConfigParser()
config.read(os.path.join(os.path.dirname(__file__), "postgres_api.ini"))

db_user=config['DEFAULT']['DB_USER']
db_password=config['DEFAULT']['DB_PASSWORD']
db_host=config['DEFAULT']['DB_HOST']
db_port=config['DEFAULT']['DB_PORT']
db_database=config['DEFAULT']['DB_DATABASE']

db_url=f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_database}"


#SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
SQLALCHEMY_DATABASE_URL = db_url 

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


