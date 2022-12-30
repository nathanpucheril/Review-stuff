from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Text, JSON, Enum
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy.sql import func

import enum

Base = declarative_base()


class User(Base):
    """User account."""

    __tablename__ = "user"

    id = Column(Integer, primary_key=True, autoincrement="auto")
    username = Column(String(255), unique=True, nullable=False)  # username does not need to be unique. may not be necessary
    email = Column(String(255), unique=True, nullable=False)
    password = Column(Text, nullable=False)
    first_name = Column(String(255))
    last_name = Column(String(255))
    last_seen = Column(DateTime)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())

    def __repr__(self):
        return f"<User {self.username}>"


class Account(Base):
    """Account."""

    __tablename__ = "account"

    id = Column(Integer, primary_key=True, autoincrement="auto")
    name = Column(Text, nullable=False)
    admin_user_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())

    admin_user = relationship("User", backref="admin_user")

    def __repr__(self):
        return f"<Account {self.name}>"


class Project(Base):
    """Project."""

    __tablename__ = "project"

    id = Column(Integer, primary_key=True, autoincrement="auto")
    name = Column(Text, nullable=False)
    description = Column(Text)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())

    account = relationship("Account", backref="account")

    def __repr__(self):
        return f"<Project {self.name}>"


class ReviewTypeEnum(enum.Enum):
    thumbs = 1
    smiles = 2
    stars = 3


class Review(Base):
    """Review."""

    __tablename__ = "review"

    id = Column(Integer, primary_key=True, autoincrement="auto")
    review_type = Column(Enum(ReviewTypeEnum))
    project_id = Column(Integer, ForeignKey("project.id"), nullable=False)
    data = Column(JSON)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())

    project = relationship("Project", backref="project")

    def __repr__(self):
        return f"<Review {self.name}>"


# def init_db(engine):
#     db_session = scoped_session(sessionmaker(autocommit=False,
#                                              autoflush=False,
#                                              bind=engine))
#     Base.query = db_session.query_property()
#     # import all modules here that might define models so that
#     # they will be registered properly on the metadata.  Otherwise
#     # you will have to import them first before calling init_db()
#     Base.metadata.create_all(bind=engine)