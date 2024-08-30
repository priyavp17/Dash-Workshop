# prompt: use a sqlalchemy  to create a database for movies


from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Create a sqlite database in memory
engine = create_engine('sqlite:///:memory:', echo=True)
Base = declarative_base()

# Define the Movie table
class Movie(Base):
  __tablename__ = 'movies'

  id = Column(Integer, primary_key=True)
  title = Column(String)
  director = Column(String)
  year = Column(Integer)

  def __repr__(self):
    return "<Movie(title='%s', director='%s', year='%s')>" % (
        self.title, self.director, self.year)

# Create the table in the database
Base.metadata.create_all(engine)

# Create a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()

# Add some movies
session.add_all([
  Movie(title='The Shawshank Redemption', director='Frank Darabont', year=1994),
  Movie(title='The Dark Knight', director='Christopher Nolan', year=2008),
  Movie(title='Pulp Fiction', director='Quentin Tarantino', year=1994)
])

# Commit the changes
session.commit()

# Query the database
for movie in session.query(Movie):
  print(movie)
