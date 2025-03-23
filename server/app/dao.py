from sqlalchemy.sql import func

from .models import Category, Course, Lesson, User, Comment, db
from .paginators import StandardResultsSetPagination, LargeResultsSetPagination


class BaseRepository:
    def __init__(self, model):
        self.model = model

    def get_all(self):
        return self.model.query.filter(self.model.is_active.__eq__(True)).all()

    def get_by_id(self, id):
        try:
            return self.model.query.get(int(id))
        except ValueError:
            return None

    def create(self, **kwargs):
        instance = self.model(**kwargs)
        instance.save()
        return instance

    def update(self, id, **kwargs):
        instance = self.model.query.get(int(id))

        if not instance:
            return None

        for key, value in kwargs.items():
            setattr(instance, key, value)

        instance.save()
        return instance


class CategoryRepository(BaseRepository):
    def __init__(self):
        super().__init__(Category)


class CourseRepository(BaseRepository):
    def __init__(self):
        super().__init__(Course)

    def get_all(
        self,
        keyword=None,
        category=None,
        page=1,
        per_page=StandardResultsSetPagination.page_size,
    ):
        query = self.model.query.filter(self.model.is_active.is_(True))

        if keyword:
            query = query.filter(self.model.title.contains(keyword))

        if category:
            query = query.filter(self.model.category_id.__eq__(category))

        query = query.order_by(self.model.date_created.desc()).paginate(
            page=page, per_page=per_page
        )

        return dict(count=query.total, results=query.items)


class LessonRepository(BaseRepository):
    def __init__(self):
        super().__init__(Lesson)

    def get_all(
        self,
        id,
        lesson=None,
        page=1,
        per_page=LargeResultsSetPagination.page_size,
    ):
        query = self.model.query.filter(
            self.model.is_active.is_(True), self.model.course_id.__eq__(id)
        )

        if lesson:
            return query.filter(self.model.id.__eq__(lesson)).first()

        query = query.order_by(self.model.date_created.desc()).paginate(
            page=page, per_page=per_page
        )

        return dict(count=query.total, results=query.items)


class UserRepository(BaseRepository):
    def __init__(self):
        super().__init__(User)

    def get_callback(self, identity):
        return self.model.query.filter_by(id=identity).one_or_none()

    def is_exists(self, email, username):
        return (
            self.model.query.filter(
                (self.model.email.__eq__(email)) | (self.model.username.__eq__(username))
            ).first()
            is not None
        )

    def auth_user(self, email, password):
        user = self.model.query.filter(self.model.email.__eq__(email)).first()
        return user if user and user.verify_password(password) else None


class CommentRepository(BaseRepository):
    def __init__(self):
        super().__init__(Comment)


class AnalyticsRepository:
    @staticmethod
    def stats_new_users():
        return (
            db.session.query(
                func.strftime("%Y-%m", User.date_created).label("month"),
                func.count(User.id).label("count"),
            )
            .group_by("month")
            .order_by("month")
            .all()
        )

    @staticmethod
    def stats_user_active():
        return (
            db.session.query(
                func.date(User.date_created).label("date"),
                func.count(User.id).label("count"),
            )
            .group_by("date")
            .order_by("date")
            .all()
        )
