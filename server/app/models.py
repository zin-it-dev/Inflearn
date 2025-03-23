from sqlalchemy import Column, Integer, Boolean, String, Text, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime, timezone

from .extensions import db
from .utils import gravatar_url
from .mixins import TimestampMixin


class Base(TimestampMixin, db.Model):
    __abstract__ = True

    is_active = Column(Boolean, default=True)

    def save(self):
        db.session.add(self)
        db.session.commit()


class User(Base, UserMixin):
    username = Column(String(80), unique=True)
    email = Column(String(100), unique=True)
    password = Column(String(255))
    avatar = Column(String(255), default=gravatar_url(email="anonymous@gmail.com"))
    first_name = Column(String(80), nullable=True)
    last_name = Column(String(80), nullable=True)
    is_admin = Column(Boolean, default=False)
    last_seen = Column(DateTime, default=datetime.now(timezone.utc))

    comments = relationship("Comment", backref="user", lazy="selectin")

    def __init__(self, *args, **kwargs):
        super(User, self).__init__(*args, **kwargs)
        self.password = generate_password_hash(kwargs.get("password"))

        if not self.avatar:
            self.avatar = gravatar_url(email=self.email)

    def verify_password(self, pwd):
        return check_password_hash(self.password, pwd)

    def __str__(self):
        return f"{self.last_name} {self.first_name}"


class Category(Base):
    name = Column(String(80), unique=True)

    courses = relationship("Course", backref="category", lazy="selectin")

    def __str__(self):
        return self.name


course_tag = db.Table(
    "course_tag",
    Column("course_id", Integer, ForeignKey("course.id"), primary_key=True),
    Column("tag_id", Integer, ForeignKey("tag.id"), primary_key=True),
)


class Tag(Base):
    name = Column(String(80), unique=True)

    def __str__(self):
        return f"#{self.name}"


class Course(Base):
    title = Column(String(80), unique=True, index=True)
    image = Column(String(255))
    description = Column(Text)

    category_id = Column(Integer, ForeignKey(Category.id), index=True)

    tags = relationship("Tag", secondary=course_tag, backref="course", lazy="selectin")
    lessons = relationship("Lesson", backref="course", lazy='selectin')
    comments = relationship("Comment", backref="course", lazy='selectin')

    @property
    def total_lessons(self):
        return len(self.lessons)

    def __str__(self):
        return self.title


lesson_tag = db.Table(
    "lesson_tag",
    Column("lesson_id", Integer, ForeignKey("lesson.id"), primary_key=True),
    Column("tag_id", Integer, ForeignKey("tag.id"), primary_key=True),
)


class Lesson(Base):
    title = Column(String(80), unique=True)
    content = Column(Text)

    course_id = Column(Integer, ForeignKey(Course.id))

    tags = relationship("Tag", secondary=lesson_tag, backref="lesson", lazy="selectin")

    def __str__(self):
        return self.title


class InteractionMixin:
    course_id = Column(Integer, ForeignKey(Course.id))
    user_id = Column(Integer, ForeignKey(User.id))


class Comment(Base, InteractionMixin):
    content = Column(Text)

    def __str__(self):
        return self.content[:20]
