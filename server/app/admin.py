from flask import redirect, url_for
from flask_admin import Admin, BaseView, expose, AdminIndexView
from flask_admin.contrib.sqla import ModelView
from flask_admin.form import SecureForm
from flask_login import current_user, logout_user
from flask_babel import Babel
from flask_admin.contrib.fileadmin import FileAdmin
from flask_admin.actions import action
from wtforms import PasswordField
from wtforms.validators import DataRequired, EqualTo
from flask_wtf.file import FileField, FileAllowed
from werkzeug.security import generate_password_hash
from markupsafe import Markup
from sqlalchemy.orm import selectinload, joinedload

from .models import db, User, Category, Course, Tag, Lesson, Comment
from .paginators import ExtraLargeResultsSetPagination
from .utils import get_locale, upload_image
from .config import file_path
from .actions import make_active
from .decorators import admin_required
from .widgets import CKTextAreaField


class SecureView(BaseView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.is_admin

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for("admin.index"))


class CommonView(ModelView, SecureView):
    form_base_class = SecureForm
    column_labels = dict(is_active="Active", is_admin="Admin")
    column_list = ["is_active", "date_created"]
    column_filters = ["is_active"]
    column_editable_list = ["is_active"]
    column_sortable_list = ["date_created"]
    create_modal = True
    edit_modal = True
    can_view_details = True
    can_export = True
    can_delete = True
    page_size = ExtraLargeResultsSetPagination.page_size

    def get_query(self):
        return (
            super()
            .get_query()
            .options(selectinload("*"))
        )

    def get_count_query(self):
        return super().get_count_query().options(selectinload("*"))

    @action(
        "activate",
        "Activate",
        "Are you sure you want to change the active status of selected models?",
    )
    def action_activate(self, ids):
        return make_active(self=self, ids=ids)


class UserView(CommonView):
    column_list = ["username", "avatar", "is_admin"] + CommonView.column_list
    column_editable_list = ["is_admin"] + CommonView.column_editable_list

    form_extra_fields = dict(
        password=PasswordField(
            "Password",
            validators=[
                DataRequired(),
                EqualTo("confirm_password", message="Passwords must match."),
            ],
        ),
        confirm_password=PasswordField("Confirm Password", validators=[DataRequired()]),
    )

    def on_model_change(self, form, model, is_created):
        if form.password.data:
            model.password = generate_password_hash(model.password)

    def _format_avatar(view, context, model, name):
        _html = f"<img src='{model.avatar}' class='img-thumbnail rounded-circle shadow-sm' alt='{model.username}'>"

        return Markup(_html)

    column_formatters = {"avatar": _format_avatar}


class CategoryView(CommonView):
    column_list = ["name", "courses"] + CommonView.column_list


class CourseView(CommonView):
    inline_models = [Tag, Lesson]
    column_list = ["title", "image", "category", "tags"] + CommonView.column_list
    column_searchable_list = ["title"]
    column_editable_list = ["title", "category", "tags"] + CommonView.column_editable_list

    form_extra_fields = {
        "image": FileField(
            "Image",
            validators=[FileAllowed(["jpg", "png"], "Only images are allowed!")],
        )
    }

    def on_model_change(self, form, model, is_created):
        if "image" in form.data and form.data["image"]:
            file = form.data["image"]
            model.image = upload_image(file)

    def _format_image(view, context, model, name):
        if not model.image:
            return "Empty"

        _html = f"<img src='{model.image}' class='img-thumbnail shadow-sm' width=80 height=80 alt='{model.title}'>"

        return Markup(_html)

    column_formatters = {"image": _format_image}

class TagView(CommonView):
    column_list = ["name", "course", "lesson"] + CommonView.column_list
    column_editable_list = ["name"] + CommonView.column_editable_list


class LessonView(CommonView):
    extra_js = ["//cdn.ckeditor.com/4.6.0/full-all/ckeditor.js"]
    form_overrides = {"content": CKTextAreaField}

    inline_models = [Tag]
    column_list = ["title", "course", "tags"] + CommonView.column_list


class CommentView(CommonView):
    column_list = ["content", "course", "user"] + CommonView.column_list
    column_searchable_list = ["content"]
    column_editable_list = [
        "user",
        "course",
    ] + CommonView.column_editable_list
    column_sortable_list = ["content"] + CommonView.column_sortable_list
    column_filters = CommonView.column_filters + ["user.username"]


class AnalyticsView(SecureView):
    @expose("/")
    def index(self):
        return self.render("admin/analytics.html")


class LogoutView(SecureView):
    @admin_required
    @expose("/")
    def index(self):
        logout_user()
        return redirect(url_for("admin.index"))


class FileView(SecureView, FileAdmin):
    pass


class AdminIndex(AdminIndexView):
    @expose("/")
    def index(self):
        return self.render(
            "admin/index.html",
        )


admin_manager = Admin(
    name="Inflearn 인프런 🎓", template_mode="bootstrap4", index_view=AdminIndex()
)
babel = Babel(locale_selector=get_locale)

admin_manager.add_view(UserView(User, db.session, category="Management"))
admin_manager.add_view(CategoryView(Category, db.session, category="Management"))
admin_manager.add_view(CourseView(Course, db.session, category="Management"))
admin_manager.add_view(LessonView(Lesson, db.session, category="Management"))
admin_manager.add_view(TagView(Tag, db.session, category="Management"))
admin_manager.add_view(CommentView(Comment, db.session, category="Management"))
admin_manager.add_view(
    AnalyticsView(name="Analytics & Statistics", endpoint="analytics-statistics")
)
admin_manager.add_view(FileView(file_path, "/static/", name="Files", category="Settings"))
admin_manager.add_view(LogoutView(name="Log Out", endpoint="logout", category="Settings"))
