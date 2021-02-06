from datetime import datetime

from sqlalchemy import Integer, Column, String, Boolean, ForeignKey, DateTime, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import validates, relationship

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(20), unique=True, nullable=False)
    password = Column(String(), nullable=False)
    timers = relationship('Timer', backref='user')

    def __str__(self):
        return "<User(username='%s')>" % self.username

    def __repr__(self):
        return self.__str__()

    @validates('username')
    def validate_username(self, key, username) -> str:
        if len(username) < 3:
            raise ValueError('Username too short')
        return username

    @validates('password')
    def validate_password(self, key, password) -> str:
        if len(password) < 6:
            raise ValueError('Password is too short')
        return password


class Timer(Base):
    __tablename__ = 'timers'
    id = Column(Integer, primary_key=True)
    timer_text = Column(Text, nullable=True)
    timer_title = Column(String(255), nullable=False)
    from_date = Column(DateTime, nullable=False, default=datetime.utcnow)
    to_date = Column(DateTime, nullable=True)
    is_private = Column(Boolean, default=False)
    is_stopped = Column(Boolean, default=False)
    user_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'), nullable=False)

    def __str__(self):
        return f'<Timer(user_id={self.user_id}, id={self.id})>'

    def __repr__(self):
        return self.__str__()

    @validates('timer_title')
    def validate_timer_title(self, key, timer_title):
        if len(timer_title) < 6:
            raise ValueError('Timer title is too short')
        return timer_title
